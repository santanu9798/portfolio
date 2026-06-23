# Render Deployment Guide for Django Portfolio

This guide will help you deploy your Django portfolio application to Render.

## Prerequisites

- A GitHub repository with your project
- A Render account (https://render.com)
- Your project pushed to GitHub

## Step-by-Step Deployment

### 1. Push Your Project to GitHub

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Create a Render Account

- Go to https://render.com
- Sign up with your GitHub account (recommended)

### 3. Create a New Web Service

1. Click on **"New +"** button in the Render dashboard
2. Select **"Web Service"**
3. Connect your GitHub repository (select the portfolio repo)
4. Fill in the configuration:
   - **Name**: portfolio (or any name you prefer)
   - **Environment**: Python 3
   - **Region**: Choose closest to your users
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --no-input`
   - **Start Command**: `gunicorn portfolio_project.wsgi:application`

### 4. Add Environment Variables

In the Render dashboard, add these environment variables:

1. **SECRET_KEY** - Generate a new one:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Copy the output and paste it as the `SECRET_KEY` value

2. **DEBUG**: `False`

3. **ALLOWED_HOSTS**: `yourdomain.onrender.com`

4. **PYTHON_VERSION**: `3.11.7`

### 5. Create a PostgreSQL Database

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Fill in:
   - **Name**: portfolio-db
   - **Database**: portfolio
   - **User**: portfolio
   - **Region**: Same as your web service
   - **PostgreSQL Version**: 15

3. Once created, copy the **Internal Database URL**
4. Go back to your Web Service settings
5. Add environment variable:
   - **DATABASE_URL**: Paste the database URL (should auto-populate)

### 6. Run Migrations

After deployment starts:

1. Go to your Web Service on Render
2. Click on the **"Shell"** tab
3. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

### 7. Enable AutoDeploy (Optional)

- In your Web Service settings, enable **"Auto-Deploy"**
- This will automatically redeploy when you push to GitHub

## Environment Variables Reference

| Variable | Value | Example |
|----------|-------|---------|
| `SECRET_KEY` | Generate using Django | `django-insecure-...` |
| `DEBUG` | Should be False | `False` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |
| `ALLOWED_HOSTS` | Your domain | `yourdomain.onrender.com` |
| `PYTHON_VERSION` | Python version to use | `3.11.7` |

## Common Issues & Solutions

### Issue: Static Files Not Loading

**Solution**: Make sure `collectstatic` runs during build:
```bash
python manage.py collectstatic --no-input
```

This is included in the build command, so it should work automatically.

### Issue: Database Connection Error

**Solution**:
1. Verify `DATABASE_URL` is set correctly
2. Check that PostgreSQL service is running
3. Run migrations: `python manage.py migrate`

### Issue: 404 Error on Homepage

**Solution**:
1. Check that `ALLOWED_HOSTS` includes your Render domain
2. Ensure URL patterns in `urls.py` are configured correctly
3. Check logs: `Log` tab in Render dashboard

### Issue: Secret Key Not Set

**Solution**:
1. Generate a new secret key locally
2. Add it to environment variables in Render dashboard
3. Restart the service

## Viewing Logs

1. Go to your Web Service on Render
2. Click the **"Logs"** tab
3. Real-time logs will show build and runtime errors

## Custom Domain (Optional)

1. In Web Service settings, click **"Custom Domain"**
2. Add your domain name
3. Follow DNS configuration instructions

## Useful Commands

After deploying, you can run commands via the Shell tab:

```bash
# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --no-input

# Run Django shell
python manage.py shell
```

## Monitoring

- **Metrics**: View CPU, Memory, and Bandwidth usage in the dashboard
- **Logs**: Real-time application logs
- **Status**: Service status page

## Need Help?

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com
- Check logs in Render dashboard for detailed error messages

Good luck with your deployment! 🚀
