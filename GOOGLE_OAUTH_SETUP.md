# Google sign-in setup

The error `401: invalid_client` means this project is using placeholder,
deleted, or incorrect Google OAuth credentials. It cannot be fixed in code:
the credentials must be created in the Google Cloud project you control.

1. Open [Google Cloud Console credentials](https://console.cloud.google.com/apis/credentials) and select or create a project.
2. Configure the OAuth consent screen. Add your Google account as a test user while the app is in testing.
3. Enable **Google Calendar API**, **Google Tasks API**, and **Gmail API** under **APIs & Services > Library**.
4. Create credentials: **OAuth client ID** > **Web application**.
5. Add this exact authorised redirect URI:

   `http://localhost:8000/api/auth/callback`

6. Copy the generated client ID and client secret into `.env`:

   ```env
   GOOGLE_CLIENT_ID=1234567890-example.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-generated-client-secret
   GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/callback
   FRONTEND_URL=http://localhost:5173
   ```

Restart the backend after saving. Do not commit `.env` or share its values.

For the app to run beyond sign-in, `.env` must also contain valid database,
Mistral, and Pinecone settings. The supplied file contains example values only.
