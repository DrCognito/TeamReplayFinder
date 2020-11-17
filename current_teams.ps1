.\.venv\Scripts\activate.ps1
$nip = @(6214973)
$summit_ga = "8161113", "7422789", "2576071", "8121295"
$summit_gb = $nip + "8077174", "8112124", "7453744"
$summit_gs = "2163", "6685591"
$summit = $summit_ga + $summit_gb + $summit_gs
$epic_extra_gb = "7556672"
$epic_playoff = "7556672", "8121295", "2576071", "8161113", "6209143"
$epic_div2 = "8077174", "6214973", "6209143", "7556672", "46", "8161113", "7118032", "2576071", "7486089", "5014799"
$teams = $epic_div2

python .\team_parse.py $teams
python .\download.py $teams