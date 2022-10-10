powershell -command "Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }"
powershell -command "Clear-History"
