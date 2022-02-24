.\.venv\Scripts\activate.ps1
$og = @("2586976")
$DPC_WEU_T2_D1 = "2163", "8599101", "8291895", "1838315", "7554697", "8605863", "8112124"
$GALAXY_DUBAI2022 = "7554697", "350190", "7119388", "1838315", "1883502", "2586976", "8291895", "8572181", "8260983", "7732977"

$teams = $og + $DPC_WEU_T2_D1 + $GALAXY_DUBAI2022 | Get-Unique
# $teams = "1838315", "2586976", "8291895", "7554697"
Write-Output("Updating replay-list for: " + $teams -join " ")

python .\team_parse_datdota.py $teams
python .\download.py $teams
Write-Output "Downloading ogscrims from googledrive"
rclone copy -P ogscrims: E:\Dota2\dbScrim\