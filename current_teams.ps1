.\.venv\Scripts\activate.ps1
$omega_league = "1883502", "36", "111474", "6214973", "2586976", "7554697", "6953913", "1838315", "2163", "39", "6685591", "8077174"
$dota_pit = "7819701", "36", "111474", "6214973", "2586976", "6685591", "7554697", "6953913" #VP.Prodigies
$teams = $omega_league

python .\team_parse.py $teams
python .\download.py $teams