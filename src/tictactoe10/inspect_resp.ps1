$t = Get-Content 'C:\Users\Antonio Esposito\Desktop\tictactoe10\resp_wpftmp.txt' -Raw
$srcs = [regex]::Matches($t, '[A-Za-z]:[^"']*\.cs"') | ForEach-Object { $_.Value }
Write-Output ('SRC_COUNT: ' + $srcs.Count)
foreach ($s in $srcs) { Write-Output ('  ' + $s) }
Write-Output ('SYSRT: ' + $t.Contains('System.Runtime.dll'))
$m = [regex]::Match($t, '/langversion:[^ ]+')
if ($m.Success) { Write-Output ('LANGV: ' + $m.Value) } else { Write-Output 'LANGV: none' }
$d = [regex]::Match($t, '/define:[^ ]+')
if ($d.Success) { Write-Output ('DEFS: ' + $d.Value) } else { Write-Output 'DEFS: none' }
$refs = [regex]::Matches($t, '/reference:"[^"]+"') | ForEach-Object { $_.Value.Split('\')[-1].Trim('"') }
Write-Output ('REF_COUNT: ' + $refs.Count)
foreach ($r in $refs) { Write-Output ('  ' + $r) }
