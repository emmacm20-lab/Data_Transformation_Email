USE B_CONTROLES

SET LANGUAGE Spanish;

DECLARE @‌PAIS CHAR(3) = 'CRI', @‌CICLO INT = 1
DECLARE @‌FECHA_PROCESO DATE = GETDATE(), @‌FECHA_PROCESO_ANT DATE = DATEADD(MONTH, -1, GETDATE())
DECLARE @‌MES_ACT NVARCHAR(20) = DATENAME(MONTH, @‌FECHA_PROCESO), @mes_ANT NVARCHAR(20) = DATENAME(MONTH, @‌FECHA_PROCESO_ANT)
DECLARE @‌SCRIPT NVARCHAR(MAX)

SET @‌SCRIPT = N'Test de Envío de Correo SQL Server - ' + CAST(@fecha_proceso AS NVARCHAR(10))

-- Construcción del cuerpo del mensaje en HTML
DECLARE @‌HTML NVARCHAR(MAX) = N'<html><body><h1>Correo de Prueba SQL Server</h1><p>Este es un mensaje de prueba enviado desde un script de SQL Server.</p><p>Detalles del Test:</p><ul><li>País: ' + @‌PAIS + '</li><li>Ciclo: ' + CAST(@ciclo AS NVARCHAR(10)) + '</li><li>Fecha Proceso: ' + CAST(@fecha_PROCESO AS NVARCHAR(10)) + '</li><li>Mes Actual: ' + @‌MES_ACT + '</li><li>Mes Anterior: ' + @‌MES_ANT + '</li></ul></body></html>'

-- Envío del correo
EXEC msdb.dbo.sp_send_dbmail
@‌profile_name = 'Alertas',
@‌recipients = 'emmanuel.c@emc-latam.com',
@‌subject = @‌SCRIPT,
@‌body = @‌HTML,
@‌body_format = 'HTML';

-- Fin del scripts