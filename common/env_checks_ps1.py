# For now I strongly not recommend using this method.
# Pyinfra hardcoded server.shell to use -c parameter, which poorly supported by PowerShell.exe.
from pyinfra.operations import server

check_arcgis = (
    r'$paths = @("C:\Program Files\ArcGIS\Pro\bin\ArcGISPro.exe", "$env:LOCALAPPDATA\Programs\ArcGIS\Pro\bin\ArcGISPro.exe"); $found = $false; foreach ($p in $paths) { if (Test-Path $p) { Write-Output "ArcGIS Pro found at: $p"; $found = $true; break } else { Write-Output "Not found at: $p" } }; if (-not $found) { Write-Output "ArcGIS Pro not found in Program Files or LocalAppData" } else { Write-Output "ArcGIS Pro check completed successfully" }'
)

server.shell(
    name="Check ArcGIS Pro & Python installation",
    commands=[
        check_arcgis
    ],
    _shell_executable="powershell.exe",
)
