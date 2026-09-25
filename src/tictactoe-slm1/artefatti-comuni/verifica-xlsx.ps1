Add-Type -AssemblyName System.IO.Compression.FileSystem
$z=[IO.Compression.ZipFile]::OpenRead((Resolve-Path 'artefatti-comuni/vendite.xlsx'))
foreach($e in $z.Entries){$r=[IO.StreamReader]::new($e.Open());$s=$r.ReadToEnd();$r.Dispose();try{[xml]$x=$s;Write-Output ($e.FullName+' OK')}catch{Write-Output ($e.FullName+' INVALID '+$_.Exception.Message)}}
$z.Dispose()
