<?php
/**
 * Jewell Services — estimate request handler (runs on Hostinger shared hosting).
 * Emails each request to the business. Set LEAD_TO below before going live.
 */
const LEAD_TO      = 'REPLACE_WITH_JEWELL_EMAIL@example.com'; // where estimate requests are delivered
const LEAD_FROM    = 'website@jewell-services.com';           // must be an address on the hosted domain
const MAX_FILES    = 5;
const MAX_FILE_MB  = 8;

header('X-Content-Type-Options: nosniff');
$wantsJson = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;

function respond($ok, $msg, $wantsJson) {
    if ($wantsJson) {
        header('Content-Type: application/json');
        http_response_code($ok ? 200 : 400);
        echo json_encode(['ok' => $ok, 'message' => $msg]);
    } else {
        header('Location: ' . ($ok ? 'thank-you/' : 'contact/?error=1'), true, 303);
    }
    exit;
}
function clean($v, $max = 2000) {
    $v = trim((string)$v);
    $v = str_replace(["\r\n", "\r"], "\n", $v);
    return mb_substr(strip_tags($v), 0, $max);
}
function oneline($v, $max = 200) { return preg_replace('/[\r\n]+/', ' ', clean($v, $max)); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') respond(false, 'Method not allowed', $wantsJson);

// Spam traps: hidden field must stay empty, and the form must take more than 3 seconds to fill in
if (!empty($_POST['company_website'])) respond(true, 'ok', $wantsJson);
$started = (int)($_POST['ts'] ?? 0);
if ($started && (time() - (int)($started / 1000)) < 3) respond(true, 'ok', $wantsJson);

$name    = oneline($_POST['name'] ?? '');
$phone   = oneline($_POST['phone'] ?? '', 40);
$email   = oneline($_POST['email'] ?? '', 120);
$service = oneline($_POST['service'] ?? '');
$zip     = oneline($_POST['zip'] ?? '', 10);
$address = oneline($_POST['address'] ?? '', 250);
$when    = oneline($_POST['timeframe'] ?? '');
$pref    = oneline($_POST['contact_pref'] ?? '');
$message = clean($_POST['message'] ?? '');
$page    = oneline($_POST['page'] ?? '', 200);

if ($name === '' || strlen(preg_replace('/\D/', '', $phone)) < 10) respond(false, 'Name and phone are required.', $wantsJson);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) $email = '';

$lines = [
    'New free estimate request from jewell-services.com',
    str_repeat('-', 44),
    "Name:      $name",
    "Phone:     $phone",
    "Email:     " . ($email ?: '-'),
    "Service:   " . ($service ?: '-'),
    "ZIP:       " . ($zip ?: '-'),
    "Address:   " . ($address ?: '-'),
    "Timeframe: " . ($when ?: '-'),
    "Contact:   " . ($pref ?: '-'),
    '',
    'Project details:',
    $message ?: '-',
    '',
    "Sent from: $page",
    'Time: ' . date('D, M j Y g:i a T'),
];
$text = implode("\n", $lines);
$subject = 'New estimate request: ' . ($service ?: 'General') . ' — ' . $name;

$boundary = 'jw_' . bin2hex(random_bytes(12));
$headers  = 'From: Jewell Services Website <' . LEAD_FROM . ">\r\n";
if ($email) $headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: multipart/mixed; boundary=\"$boundary\"\r\n";

$body  = "--$boundary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n\r\n$text\r\n";

if (!empty($_FILES['photos']) && is_array($_FILES['photos']['name'])) {
    $allowed = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/heic' => 'heic', 'image/heif' => 'heif'];
    $count = 0;
    foreach ($_FILES['photos']['name'] as $i => $orig) {
        if ($count >= MAX_FILES) break;
        if ($_FILES['photos']['error'][$i] !== UPLOAD_ERR_OK) continue;
        if ($_FILES['photos']['size'][$i] > MAX_FILE_MB * 1024 * 1024) continue;
        $tmp  = $_FILES['photos']['tmp_name'][$i];
        $mime = function_exists('mime_content_type') ? mime_content_type($tmp) : $_FILES['photos']['type'][$i];
        if (!isset($allowed[$mime])) continue;
        $fname = 'photo-' . ($count + 1) . '.' . $allowed[$mime];
        $body .= "--$boundary\r\nContent-Type: $mime; name=\"$fname\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"$fname\"\r\n\r\n";
        $body .= chunk_split(base64_encode(file_get_contents($tmp))) . "\r\n";
        $count++;
    }
}
$body .= "--$boundary--";

$sent = @mail(LEAD_TO, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers, '-f' . LEAD_FROM);

// Keep a private backup log in case email delivery fails (folder is blocked from the web by .htaccess)
$dir = __DIR__ . '/_leads';
if (!is_dir($dir)) @mkdir($dir, 0700, true);
@file_put_contents($dir . '/leads-' . date('Y-m') . '.log', $text . "\nEmailed: " . ($sent ? 'yes' : 'NO') . "\n\n", FILE_APPEND | LOCK_EX);

respond((bool)$sent, $sent ? 'ok' : 'Mail failed', $wantsJson);
