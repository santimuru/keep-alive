# keep-alive

GitHub Actions workflow que hace ping a los proyectos de Streamlit Community Cloud cada 9 horas para evitar que entren en modo sleep.

Corre automáticamente a las **00:00, 09:00 y 18:00 UTC**. No requiere ninguna configuración ni que la PC esté encendida.

## Proyectos activos

| Proyecto | URL |
|---|---|
| Telecom Churn · Survival Analysis | telecom-churn-survival-santiagomuru.streamlit.app |
| Customer Review Intelligence | customer-review-intelligence-santiagomuru.streamlit.app |
| Customer Lifetime Value Prediction | customer-clv-prediction-santiagomuru.streamlit.app |
| Tokyo Real Estate Explorer | tokyo-real-estate-explorer-santiagomuru.streamlit.app |

## Agregar un proyecto nuevo

Editar `.github/workflows/keep-alive.yml` y agregar un step al final del job `ping`:

```yaml
- name: Nombre del proyecto
  continue-on-error: true
  run: |
    curl --max-time 60 --silent --output /dev/null --write-out "Status: %{http_code}\n" \
      https://tu-app-url.streamlit.app
```

## Correr manualmente

Ir a [Actions](../../actions) → "Keep Streamlit Apps Alive" → "Run workflow".
