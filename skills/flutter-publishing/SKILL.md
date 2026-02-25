---
name: flutter-publishing
description: Step-by-step guides and prompts for preparing and publishing Flutter apps to the Google Play Store and Apple App Store using AI coding tools. Includes setup instructions for Android and iOS release builds, code signing, and App Store Connect / Google Play Console configuration. Use when a user asks to release, publish, or build a production bundle for their Flutter app.
---

# Flutter App Publishing Playbook

This skill provides step-by-step procedures and prompts to assist developers in preparing their Flutter applications for release to both the Google Play Store and the Apple App Store.

## Prerequisites & External Resources

- **Google Antigravity:** https://antigravity.google/
- **Google Stitch:** https://stitch.withgoogle.com/
- **Flutter MCP server:** https://docs.flutter.dev/ai/mcp-server
- **Stitch Skills:** https://github.com/google-labs-code/stitch-skills/tree/main
- **Stitch MCP server:** https://stitch.withgoogle.com/docs/mcp/setup

**Stitch MCP server install script:**
```json
{
  "mcpServers": {
    "stitch": {
      "serverUrl": "https://stitch.googleapis.com/mcp",
      "headers": {
        "X-Goog-Api-Key": "YOUR-API-KEY"
      }
    }
  }
}
```

---

## ▶ PLAY STORE (Android)

### Step 1: Build your release bundle (Automated via AI)
Tell Claude Code or AntiGravity to prepare your Flutter app for release. This includes setting the app ID, versioning, creating a signing key, configuring Gradle, and building the `.aab` file. The AI agent can handle all of this for you.

**Draft Prompt for Agent:**
> "Prepare my Flutter app for Google Play Store release. Set a unique applicationId, configure versionCode and versionName, generate a signing keystore, set up signing in `build.gradle` with a `key.properties` file, and build a release `.aab` file using `flutter build appbundle`. Make sure targetSdkVersion meets current Play Store requirements."

### Step 2: Set up Google Play Console (Manual)
- Go to [play.google.com/console](https://play.google.com/console) and pay the one-time $25 dev fee.
- Create a new app and fill in the basics (name, language, free/paid).
- Complete the store listing: description, screenshots, feature graphic (1024×500), app icon (512×512), privacy policy URL.
- Fill in the content rating questionnaire and data safety section.

### Step 3: Upload and submit for review
- Go to Release > Production (or better yet, start with Internal Testing).
- Create a new release and upload the `.aab` file your tool built.
- Add release notes and hit Send for review.

*First review typically takes a few days to a week. After that, updates usually go through in hours. Internal test track is instant with no review wait — great for verifying on real devices before going live.*

---

## 🍏 APP STORE (iOS)

### Step 1: Build your release bundle (Automated via AI)
Tell Claude Code or AntiGravity to prepare your Flutter app for iOS release. This includes configuring the bundle identifier, versioning, setting up code signing, and building the release archive.

**Draft Prompt for Agent:**
> "Prepare my Flutter app for Apple App Store release. Set a unique bundle identifier, configure the version and build number, set up code signing with automatic signing in Xcode, and build a release archive using `flutter build ipa`. Make sure the deployment target meets current App Store requirements."

**Note:** You will need an Apple Developer account ($99/year) and a Mac to build for iOS. Code signing ultimately requires Xcode, so the AI tool will need to be running on macOS.

### Step 2: Set up App Store Connect (Manual)
- Go to [appstoreconnect.apple.com](https://appstoreconnect.apple.com) and sign in with your Apple Developer account.
- Create a new app and fill in the basics (name, bundle ID, SKU, primary language).
- Complete the store listing: description, keywords, screenshots (for each device size), app icon (1024×1024), privacy policy URL.
- Fill in the age rating questionnaire.
- Complete the App Privacy section (similar to Play Store's data safety).

### Step 3: Upload and submit for review
- Open the `.ipa` file your tool built and upload it via Transporter (Mac app) or directly through Xcode.
- In App Store Connect, select your build, add release notes, and hit Submit for Review.

*First review typically takes 1–2 days but can take longer. You can use TestFlight for internal and external beta testing before going live — internal testers get access instantly, external testers need a brief review.*
