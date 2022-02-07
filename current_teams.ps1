.\.venv\Scripts\activate.ps1
$og = @("2586976")
$DPC_WEU_T1_D1 = "7554697", "111474", "2163", "1838315", "8291895", "8599101", "8598999"
$OGA_DOTAPIT_S5_EU = "7119388", "36", "8291895", "7554697", "2163", "1838315", "111474"
$DPC_WEU_FINAL = "2163", "8599101", "8291895"

$teams = $og + $DPC_WEU_FINAL | Get-Unique
# $teams = "1838315", "2586976", "8291895", "7554697"
Write-Output("Updating replay-list for: " + $teams -join " ")

python .\team_parse_datdota.py $teams
python .\download.py $teams
Write-Output "Downloading ogscrims from googledrive"
rclone copy -P ogscrims: E:\Dota2\dbScrim\