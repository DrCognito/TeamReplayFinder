.\.venv\Scripts\activate.ps1
$og = @("2586976")
$DPC_WEU_T2_D1 = "2163", "8599101", "8291895", "1838315", "7554697", "8605863", "8112124"
$GALAXY_DUBAI2022 = "7554697", "350190", "7119388", "1838315", "1883502", "2586976", "8291895", "8572181", "8260983", "7732977"

$GALAXY_DUBAI2022_G1 = "7554697", "350190", "7119388", "8260983", "8291895"
# OG group
$GALAXY_DUBAI2022_G2 = "1838315", "1883502", "8572181", "7732977"

$STOCKHOLM_DPC_2022 = "2586976", "2163", "8599101", "8291895", "350190", "7732977", "8214850", "39", "8260983", "7391077", "8254400", "8721219", "7119388"
$STOCKHOLM_DPC_GROUPA = "2586976", "8254400", "7732977", "8214850", "8291895", "39", "8721219"
$STOCKHOLM_DPC_GROUPB = "8599101", "2163", "7119388", "350190", "7391077", "8260983"

$testing = 2586976

#$teams = $og + $GALAXY_DUBAI2022_G2 | Get-Unique
$teams = $og + $STOCKHOLM_DPC_2022 | Get-Unique
# $teams = "1838315", "2586976", "8291895", "7554697"
Write-Output("Updating replay-list for: " + $teams -join " ")

python .\team_parse_datdota.py $teams
python .\download.py $teams
Write-Output "Downloading ogscrims from googledrive"
rclone copy -P ogscrims: E:\Dota2\dbScrim\