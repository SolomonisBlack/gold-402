<?php
/**
 * Jewell Services — estimate request handler (runs on Hostinger shared hosting).
 * Emails each request to the business and keeps a private backup log.
 *
 * BEFORE LAUNCH: set LEAD_TO to Jewell's inbox, and create the LEAD_FROM mailbox
 * in hPanel (Emails) so messages pass SPF/DKIM and don't land in spam.
 */
const LEAD_TO     = 'solomon.dzukey@gmail.com';        // TESTING inbox — change to Jewell's email before launch
const LEAD_FROM   = 'website@jewell-services.com';     // must be a mailbox on the hosted domain
const MAX_FILES   = 5;
const MAX_TOTAL_MB = 20;
const RATE_LIMIT  = 5;     // max submissions per IP...
const RATE_WINDOW = 600;   // ...per 10 minutes

date_default_timezone_set('America/Chicago');
header('X-Content-Type-Options: nosniff');
$wantsJson = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;

function respond($ok, $msg, $wantsJson) {
    if ($wantsJson) {
        header('Content-Type: application/json');
        http_response_code($ok ? 200 : 400);
        echo json_encode(['ok' => $ok, 'message' => $msg]);
    } else {
        header('Location: ' . ($ok ? 'thank-you/' : 'contact/?error=1#estimate'), true, 303);
    }
    exit;
}
function clean($v, $max = 2000) {
    $v = str_replace(["\r\n", "\r"], "\n", trim((string)$v));
    return mb_substr(strip_tags($v), 0, $max);
}
function oneline($v, $max = 200) { return trim(preg_replace('/[\r\n\t]+/', ' ', clean($v, $max))); }

// Private log folder: outside public_html when possible, otherwise a web-blocked folder.
function lead_dir() {
    $outside = dirname($_SERVER['DOCUMENT_ROOT'] ?? __DIR__) . '/jewell_leads';
    if ((is_dir($outside) || @mkdir($outside, 0700, true)) && is_writable($outside)) return $outside;
    $inside = __DIR__ . '/_leads';
    if (!is_dir($inside)) @mkdir($inside, 0700, true);
    if (!file_exists($inside . '/.htaccess')) @file_put_contents($inside . '/.htaccess', "Require all denied\nDeny from all\n");
    return $inside;
}
function log_line($file, $text) {
    if (@file_put_contents(lead_dir() . '/' . $file, $text . "\n\n", FILE_APPEND | LOCK_EX) === false) {
        error_log('[jewell] could not write lead log ' . $file);
    }
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') respond(false, 'Method not allowed', $wantsJson);

// Uploads larger than post_max_size arrive with an empty $_POST
if (empty($_POST) && (int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 0) respond(false, 'Upload too large', $wantsJson);

if (strpos(LEAD_TO, 'example.com') !== false || !filter_var(LEAD_TO, FILTER_VALIDATE_EMAIL)) {
    error_log('[jewell] LEAD_TO is not configured');
    respond(false, 'Form not configured', $wantsJson);
}

// Same-site check (blocks most drive-by bots posting from elsewhere)
$origin = $_SERVER['HTTP_ORIGIN'] ?? ($_SERVER['HTTP_REFERER'] ?? '');
$host = $_SERVER['HTTP_HOST'] ?? '';
if ($origin && $host && parse_url($origin, PHP_URL_HOST) !== $host) respond(false, 'Bad origin', $wantsJson);

// Rate limit per IP
$ip = $_SERVER['REMOTE_ADDR'] ?? '0';
$rlFile = lead_dir() . '/rate-' . md5($ip) . '.json';
$hits = array_filter((array)json_decode((string)@file_get_contents($rlFile), true), function ($t) { return $t > time() - RATE_WINDOW; });
if (count($hits) >= RATE_LIMIT) respond(false, 'Too many requests', $wantsJson);
$hits[] = time();
@file_put_contents($rlFile, json_encode(array_values($hits)), LOCK_EX);

$name    = oneline($_POST['name'] ?? '', 120);
$phone   = oneline($_POST['phone'] ?? '', 40);
$email   = oneline($_POST['email'] ?? '', 120);
$service = oneline($_POST['service'] ?? '');
$zip     = oneline($_POST['zip'] ?? '', 60);
$address = oneline($_POST['address'] ?? '', 250);
$company = oneline($_POST['business'] ?? '', 150);
$when    = oneline($_POST['timeframe'] ?? '');
$pref    = oneline($_POST['contact_pref'] ?? '');
$single  = !empty($_POST['single_mom']) ? 'YES — apply 10% single-mother discount' : '';
$message = clean($_POST['message'] ?? '');
$page    = oneline($_POST['page'] ?? '', 200);

if ($name === '' || strlen(preg_replace('/\D/', '', $phone)) < 10) respond(false, 'Name and phone are required.', $wantsJson);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) $email = '';

$lines = [
    'New free estimate request from the Jewell Services website',
    str_repeat('-', 44),
    "Name:      $name",
    "Phone:     $phone",
    "Email:     " . ($email ?: '-'),
    "Service:   " . ($service ?: '-'),
    "City/ZIP:  " . ($zip ?: '-'),
];
if ($company) $lines[] = "Business:  $company";
if ($address) $lines[] = "Address:   $address";
if ($when)    $lines[] = "Timeframe: $when";
if ($pref)    $lines[] = "Contact:   $pref";
if ($single)  $lines[] = "Discount:  $single";
array_push($lines, '', 'Project details:', $message ?: '-', '', "Sent from: $page", 'Time: ' . date('D, M j Y g:i a T'));
$text = implode("\n", $lines);

// Spam signals: hidden field filled, or the form was completed impossibly fast.
// Never drop silently — log it so a real lead can still be recovered.
$elapsed = isset($_POST['elapsed']) && is_numeric($_POST['elapsed']) ? (int)$_POST['elapsed'] : -1;
$honeypot = trim((string)($_POST['hp_x7'] ?? '')) !== '';
if ($honeypot || ($elapsed >= 0 && $elapsed < 1500)) {
    log_line('spam-' . date('Y-m') . '.log', $text . "\nReason: " . ($honeypot ? 'honeypot' : "fast ($elapsed ms)"));
    respond(true, 'ok', $wantsJson);
}

$subject = 'New estimate request: ' . ($service ?: 'General') . ' — ' . $name;
$boundary = 'jw_' . bin2hex(random_bytes(12));
$headers  = 'From: Jewell Services Website <' . LEAD_FROM . ">\r\n";
if ($email) {
    $safeName = trim(preg_replace('/[,;:"<>\\\\]/', '', $name));
    $headers .= 'Reply-To: ' . mb_encode_mimeheader($safeName, 'UTF-8', 'Q') . " <$email>\r\n";
}
$headers .= "MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=\"$boundary\"\r\n";
$body = "--$boundary\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n\r\n$text\r\n";

$attached = 0;
if (!empty($_FILES['photos']) && is_array($_FILES['photos']['name'])) {
    $allowed = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/heic' => 'heic', 'image/heif' => 'heif'];
    $total = 0;
    foreach ($_FILES['photos']['name'] as $i => $orig) {
        if ($attached >= MAX_FILES) break;
        if ($_FILES['photos']['error'][$i] !== UPLOAD_ERR_OK) continue;
        $size = (int)$_FILES['photos']['size'][$i];
        if ($total + $size > MAX_TOTAL_MB * 1024 * 1024) break;
        $tmp  = $_FILES['photos']['tmp_name'][$i];
        $mime = function_exists('mime_content_type') ? mime_content_type($tmp) : $_FILES['photos']['type'][$i];
        if (!isset($allowed[$mime])) continue;
        $fname = 'photo-' . ($attached + 1) . '.' . $allowed[$mime];
        $body .= "--$boundary\r\nContent-Type: $mime; name=\"$fname\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"$fname\"\r\n\r\n";
        $body .= chunk_split(base64_encode(file_get_contents($tmp))) . "\r\n";
        $total += $size;
        $attached++;
    }
}
$body .= "--$boundary--";

$sent = @mail(LEAD_TO, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers, '-f' . LEAD_FROM);
log_line('leads-' . date('Y-m') . '.log', $text . "\nPhotos: $attached\nEmailed: " . ($sent ? 'yes' : 'NO'));

respond((bool)$sent, $sent ? 'ok' : 'Mail failed', $wantsJson);
