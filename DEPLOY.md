# Deploy Checklist

## 1. Push to GitHub

```powershell
git init
git add .
git commit -m "Prepare app for deployment"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 2. Deploy on Render

1. Create a new Render account and connect GitHub.
2. Choose `New +` -> `Blueprint`.
3. Select this repository.
4. Render will read `render.yaml` automatically.
5. Set the final public hostname values after the first deploy:
   - `ALLOWED_HOSTS`
   - `CSRF_TRUSTED_ORIGINS`

## 3. Required environment variables

Render already creates:

- `SECRET_KEY`
- `DATABASE_URL`

You should confirm:

- `DEBUG=False`
- `ALLOWED_HOSTS=your-app.onrender.com`
- `CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com`

## 4. Notes

- Do not upload `.venv`, `venv`, `db.sqlite3`, `.env`, or log files.
- `build.sh` will install packages, collect static files, and run migrations.
- The production server uses `gunicorn`.
