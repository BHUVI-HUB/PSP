# Harmful

log_severity = None
if 'severity' in configuration:
log_severity = configuration['severity']
else:
log_severity = 'Info'


#Idiomatic

log_severity = configuration.get('severity', 'Info')
