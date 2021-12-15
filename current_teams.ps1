.\.venv\Scripts\activate.ps1
$og = @("2586976")
$DPC_WEU_T1_D1 = "7554697", "111474", "2163", "1838315", "8291895", "8599101", "8598999"
$OGA_DOTAPIT_S5_EU = "7119388", "36", "8291895", "7554697", "2163", "1838315", "111474"

$teams = $og + $DPC_WEU_T1_D1 + $OGA_DOTAPIT_S5_EU | Get-Unique
Write-Output "Processing " $teams

python .\team_parse.py $teams
python .\download.py $teams 