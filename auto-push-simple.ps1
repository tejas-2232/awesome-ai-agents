Write-Host "=== Interactive Auto-push Monitor ===" -ForegroundColor Green
Write-Host "You'll be prompted for commit messages when changes are detected" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow

while ($true) {
    Start-Sleep -Seconds 2
    
    $status = git status --porcelain
    
    if ($status) {
        Write-Host "`n>> Changes detected:" -ForegroundColor Yellow
        Write-Host $status
        
        # Prompt for custom commit message
        Write-Host "`n>> Enter commit message (or press Enter for auto-generated):" -ForegroundColor Cyan
        $userMessage = Read-Host
        
        if ([string]::IsNullOrWhiteSpace($userMessage)) {
            # Generate auto message if no input
            $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $commitMessage = "Auto update: $timestamp"
        } else {
            $commitMessage = $userMessage
        }
        
        git add -A
        git commit -m $commitMessage
        
        Write-Host ">> Committed: $commitMessage" -ForegroundColor Green
        
        # Ask if user wants to push
        $pushChoice = Read-Host ">> Push to GitHub? (Y/n)"
        if ($pushChoice -eq "" -or $pushChoice -eq "y" -or $pushChoice -eq "Y") {
            Write-Host ">> Pushing to GitHub..." -ForegroundColor Blue
            
            $pushResult = git push origin main 2>&1
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host ">> Successfully pushed!" -ForegroundColor Green
            } else {
                Write-Host ">> Push failed: $pushResult" -ForegroundColor Red
                Write-Host ">> Changes committed locally" -ForegroundColor Yellow
            }
        } else {
            Write-Host ">> Skipped push - changes saved locally" -ForegroundColor Yellow
        }
        
        Write-Host "------------------------" -ForegroundColor Gray
    }
}
