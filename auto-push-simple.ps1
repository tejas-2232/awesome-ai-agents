Write-Host "=== Auto-push monitor started ===" -ForegroundColor Green
Write-Host "Watching for file changes... (Ctrl+C to stop)" -ForegroundColor Cyan

while ($true) {
    Start-Sleep -Seconds 2
    
    $status = git status --porcelain
    
    if ($status) {
        Write-Host ">> Changes detected:" -ForegroundColor Yellow
        Write-Host $status
        
        git add -A
        
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        git commit -m "Auto update: $timestamp"
        
        Write-Host ">> Pushing to GitHub..." -ForegroundColor Blue
        git push origin main
        
        Write-Host ">> Successfully pushed!" -ForegroundColor Green
        Write-Host "------------------------" -ForegroundColor Gray
    }
}
