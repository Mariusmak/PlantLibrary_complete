[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$CommandLine,

    [Parameter(Mandatory = $true)]
    [string]$LogPath,

    [ValidateRange(1, 200)]
    [int]$TailLines = 20
)

$resolvedLogPath = if ([System.IO.Path]::IsPathRooted($LogPath)) {
    [System.IO.Path]::GetFullPath($LogPath)
} else {
    [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $LogPath))
}

$logDirectory = Split-Path -Parent $resolvedLogPath
if ($logDirectory -and -not (Test-Path -LiteralPath $logDirectory)) {
    New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null
}

$shellPath = (Get-Process -Id $PID).Path
$startedAt = [System.Diagnostics.Stopwatch]::StartNew()

& $shellPath -NoLogo -NoProfile -NonInteractive -Command $CommandLine 2>&1 |
    Tee-Object -FilePath $resolvedLogPath |
    Out-Null
$commandExitCode = $LASTEXITCODE
$startedAt.Stop()

if ($null -eq $commandExitCode) {
    $commandExitCode = 0
}

$tail = @()
if (Test-Path -LiteralPath $resolvedLogPath) {
    $tail = [string[]]@(Get-Content -LiteralPath $resolvedLogPath -Tail $TailLines)
}

[pscustomobject]@{
    command = $CommandLine
    exit_code = $commandExitCode
    duration_ms = $startedAt.ElapsedMilliseconds
    log_path = $resolvedLogPath
    tail = $tail
} | ConvertTo-Json -Compress

exit $commandExitCode
