{{/* Chart name */}}
{{- define "producer.name" -}}
{{ .Chart.Name }}
{{- end }}

{{/* Full name used for Services, Deployments, etc. */}}
{{- define "producer.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{ .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end -}}
{{- end }}
