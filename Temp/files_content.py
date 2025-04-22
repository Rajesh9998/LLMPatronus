LICENSE = '''
MIT License

Copyright (c) 2020 Rewanth Cool

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

README = '''

# Vuldroid
	
  ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg) ![supports Android](https://img.shields.io/badge/Android-4630EB.svg?style=flat-square&logo=ANDROID&labelColor=A4C639&logoColor=fff)<p><a href="https://twitter.com/akshanshjaiswl"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" height=25></a> <a href="https://medium.com/@akshanshjaiswal"><img src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" height=25></a> 
</p>
Vuldroid is a Vulnerable Android Application made with security issues in order to demonstrate how they can occur in code.


<img src="https://github.com/jaiswalakshansh/Vuldroid/raw/master/images/logo.png" align="centre" height="600" width="395"><img src="https://github.com/jaiswalakshansh/Vuldroid/blob/master/images/screen1.png" align="centre" height="600" width="395"><img src="https://github.com/jaiswalakshansh/Vuldroid/blob/master/images/screen3.png" align="right" height="600" width="320">





## Vulnerabilities Covered:
- Code Execution via Malicious App
- Steal Files via Webview using XHR request
- Steal Files using Fileprovider via Intents
- Steal Password ResetTokens/MagicLoginLinks
- Webview Xss via Exported Activity
- Webview Xss via DeepLink
- Intent Sniffing Between Two Applications
- Reading User Email via Broadcasts

## To Get started:
 - Install the APK from the [repository](https://github.com/jaiswalakshansh/Vuldroid/blob/master/Apks/Vuldroid.apk?raw=true) and play around
 - Find the areas where you think this can be exploited
 - I have also written a [blog](https://medium.com/@akshanshjaiswal/vuldroid-app-walkthrough-8f8e4511cad5?sk=45daf0e7fcf7de3f6a92fe8574c070a9) that you can refer as walkthrough but make sure you try yourself first
 - If you want to use your own firebase project for authentication clone the repo and remove the google-services.json and add your project one.




'''

build = '''
// Top-level build file where you can add configuration options common to all sub-projects/modules.
buildscript {
    repositories {
        google()
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:4.0.2'
        classpath 'com.google.gms:google-services:4.3.3'

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}

allprojects {
    repositories {
        google()
        jcenter()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
'''

gradle = '''
# Project-wide Gradle settings.
# IDE (e.g. Android Studio) users:
# Gradle settings configured through the IDE *will override*
# any settings specified in this file.
# For more details on how to configure your build environment visit
# http://www.gradle.org/docs/current/userguide/build_environment.html
# Specifies the JVM arguments used for the daemon process.
# The setting is particularly useful for tweaking memory settings.
org.gradle.jvmargs=-Xmx2048m
# When configured, Gradle will run in incubating parallel mode.
# This option should only be used with decoupled projects. More details, visit
# http://www.gradle.org/docs/current/userguide/multi_project_builds.html#sec:decoupled_projects
# org.gradle.parallel=true
# AndroidX package structure to make it clearer which packages are bundled with the
# Android operating system, and which are packaged with your app"s APK
# https://developer.android.com/topic/libraries/support-library/androidx-rn
android.useAndroidX=true
# Automatically convert third-party libraries to use AndroidX
android.enableJetifier=true
'''

gradlew = '''
#!/usr/bin/env sh

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=`dirname "$PRG"`"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=`basename "$0"`

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS=""

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*"
}

die () {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar

# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=`ulimit -H -n`
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin, switch paths to Windows format before running java
if $cygwin ; then
    APP_HOME=`cygpath --path --mixed "$APP_HOME"`
    CLASSPATH=`cygpath --path --mixed "$CLASSPATH"`
    JAVACMD=`cygpath --unix "$JAVACMD"`

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=`find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null`
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=`echo "$arg"|egrep -c "$OURCYGPATTERN" -`
        CHECK2=`echo "$arg"|egrep -c "^-"`                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                    ### Added a condition
            eval `echo args$i`=`cygpath --path --ignore --mixed "$arg"`
        else
            eval `echo args$i`="\"$arg\""
        fi
        i=$((i+1))
    done
    case $i in
        (0) set -- ;;
        (1) set -- "$args0" ;;
        (2) set -- "$args0" "$args1" ;;
        (3) set -- "$args0" "$args1" "$args2" ;;
        (4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        (5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        (6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        (7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        (8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        (9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save () {
    for i do printf %s\\n "$i" | sed "s/'/'\\\\''/g;1s/^/'/;\$s/\$/' \\\\/" ; done
    echo " "
}
APP_ARGS=$(save "$@")

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\"-Dorg.gradle.appname=$APP_BASE_NAME\"" -classpath "\"$CLASSPATH\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

# by default we should be in the correct project dir, but when run from Finder on Mac, the cwd is wrong
if [ "$(uname)" = "Darwin" ] && [ "$HOME" = "$PWD" ]; then
  cd "$(dirname "$0")"
fi

exec "$JAVACMD" "$@"

'''

gradlew = '''
@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar

@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%GRADLE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega

'''

local = '''
## This file is automatically generated by Android Studio.
# Do not modify this file -- YOUR CHANGES WILL BE ERASED!
#
# This file should *NOT* be checked into Version Control Systems,
# as it contains information specific to your local configuration.
#
# Location of the SDK. This is only used by Gradle.
# For customization when using a Version Control System, please read the
# header note.
sdk.dir=/root/Android/Sdk
'''

settings = '''
include ':app'
rootProject.name = "vuldroid"
'''

_gitignore = '''
/build
'''

build = '''
apply plugin: 'com.android.application'
apply plugin: 'com.google.gms.google-services'

android {
    compileSdkVersion 29
    buildToolsVersion "29.0.3"

    defaultConfig {
        applicationId "com.vuldroid.application"
        minSdkVersion 21
        targetSdkVersion 29
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar"])
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'com.karumi:dexter:6.2.2'
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    implementation 'com.google.firebase:firebase-auth:19.3.2'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'androidx.test.ext:junit:1.1.1'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
    implementation 'androidx.cardview:cardview:1.0.0'
    implementation 'com.google.android.material:material:1.1.0'

}

'''

google_services = '''
{
  "project_info": {
    "project_number": "532379372471",
    "firebase_url": "https://vuldroid-app.firebaseio.com",
    "project_id": "vuldroid-app",
    "storage_bucket": "vuldroid-app.appspot.com"
  },
  "client": [
    {
      "client_info": {
        "mobilesdk_app_id": "1:532379372471:android:b5691c4c4de28983327632",
        "android_client_info": {
          "package_name": "com.vuldroid.application"
        }
      },
      "oauth_client": [
        {
          "client_id": "532379372471-8hlstagdlqafiarpcluuaqctapvs31jb.apps.googleusercontent.com",
          "client_type": 3
        }
      ],
      "api_key": [
        {
          "current_key": ""
        }
      ],
      "services": {
        "appinvite_service": {
          "other_platform_oauth_client": [
            {
              "client_id": "532379372471-8hlstagdlqafiarpcluuaqctapvs31jb.apps.googleusercontent.com",
              "client_type": 3
            }
          ]
        }
      }
    }
  ],
  "configuration_version": "1"
}
'''

proguard_rules = '''
# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# If your project uses WebView with JS, uncomment the following
# and specify the fully qualified class name to the JavaScript interface
# class:
#-keepclassmembers class fqcn.of.javascript.interface.for.webview {
#   public *;
#}

# Uncomment this to preserve the line number information for
# debugging stack traces.
#-keepattributes SourceFile,LineNumberTable

# If you keep the line number information, uncomment this to
# hide the original source file name.
#-renamesourcefileattribute SourceFile
'''

ExampleInstrumentedTest = '''
package com.vuldroid.application;

import android.content.Context;

import androidx.test.platform.app.InstrumentationRegistry;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.*;

/**
 * Instrumented test, which will execute on an Android device.
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
    @Test
    public void useAppContext() {
        // Context of the app under test.
        Context appContext = InstrumentationRegistry.getInstrumentation().getTargetContext();
        assertEquals("com.vuldroid.application", appContext.getPackageName());
    }
}
'''

AndroidManifest = '''
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.vuldroid.application">

    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:requestLegacyExternalStorage="true"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        android:usesCleartextTraffic="true">
        <activity android:name=".RootDetection"></activity>
        <activity
            android:name=".RoutingActivity"
            android:exported="true" />
        <activity android:name=".EmailViewer" />

        <receiver
            android:name=".MyReceiver"
            android:enabled="true"
            android:exported="true">
            <intent-filter>
                <action android:name="com.example.Broadcast" />
            </intent-filter>
        </receiver> <!-- register the service -->
        <activity android:name=".SendMsgtoApp" />
        <activity
            android:name=".NotesViewer"
            android:exported="false" />
        <activity android:name=".BlogsViewer">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <data
                    android:host="medium.com"
                    android:scheme="http" />
                <data
                    android:host="medium.com"
                    android:scheme="https" />
            </intent-filter>
        </activity>
        <activity android:name=".YoutubeViewer">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
            </intent-filter>
        </activity>
        <activity android:name=".RequestPassword" />
        <activity android:name=".ForgetPassword">
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <data
                    android:host="*.firebaseapp.com"
                    android:scheme="https" />
            </intent-filter>
        </activity>
        <activity
            android:name=".Dashboard"
            android:exported="false" />
        <activity android:name=".Signup" />
        <activity android:name=".Login" />
        <activity android:name=".UserLogin" />
        <activity android:name=".SplashScreen">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <meta-data
            android:name="preloaded_fonts"
            android:resource="@array/preloaded_fonts" />

        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="${applicationId}.provider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/provider_paths" />
        </provider>
    </application>

</manifest>
'''

BlogsViewer = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class BlogsViewer extends AppCompatActivity {
    String gettoken;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_blogsviewer);
        Bundle extras = getIntent().getExtras();
        if(extras == null){
             WebView vulnerable =(WebView) findViewById(R.id.loads);
            WebSettings webSettings = vulnerable.getSettings();
            webSettings.setJavaScriptEnabled(true);
            webSettings.setAllowFileAccessFromFileURLs(true);
            vulnerable.setWebChromeClient(new WebChromeClient());
            WebViewClientImpl webViewClient = new WebViewClientImpl(this);
            vulnerable.setWebViewClient(webViewClient);
            vulnerable.loadUrl("https://medium.com"); }

            else{gettoken=getIntent().getData().getQueryParameter("url");
            WebView vulnerable =(WebView) findViewById(R.id.loads);
            WebSettings webSettings = vulnerable.getSettings();
            webSettings.setJavaScriptEnabled(true);
            webSettings.setAllowFileAccess(true);
            webSettings.setAllowFileAccessFromFileURLs(true);
            webSettings.setAllowUniversalAccessFromFileURLs(true);
            vulnerable.setWebChromeClient(new WebChromeClient());
            WebViewClientImpl webViewClient = new WebViewClientImpl(this);
            vulnerable.setWebViewClient(webViewClient);
            vulnerable.loadUrl(gettoken);}

    }}
    class WebViewClientImpl extends WebViewClient {

        private Activity activity = null;

        public WebViewClientImpl(Activity activity) {
            this.activity = activity;
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView webView, String url) {
            return false;

        }

    }


'''

Dashboard = '''
package com.vuldroid.application;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;

public class Dashboard extends AppCompatActivity {

    @Override
    public void onBackPressed() {
        new AlertDialog.Builder(this)
                .setTitle("Really Exit?")
                .setMessage("Are you sure you want to exit?")
                .setNegativeButton(android.R.string.no, null)
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {

                    public void onClick(DialogInterface arg0, int arg1) {
                        Dashboard.super.onBackPressed();
                        System.exit(0);
                    }
                }).create().show();
    }

    public void youtubeview(View view){
        Intent intent =new Intent(getApplicationContext(), YoutubeViewer.class);
        startActivity(intent);
    }

    public void blogsview(View view){
        Intent intent =new Intent(getApplicationContext(), BlogsViewer.class);
        startActivity(intent);
    }

    public void notesview(View view){
        Intent intent =new Intent(getApplicationContext(), NotesViewer.class);
        startActivity(intent);
    }
    public void sendmsgtoapp(View view){
        Intent intent =new Intent(getApplicationContext(),SendMsgtoApp.class);
        startActivity(intent);
    }



    public  void emailview(View v){
        Intent intent =new Intent(getApplicationContext(), EmailViewer.class);
        startActivity(intent);
    }

    public  void rootview(View v){
        Intent intent =new Intent(getApplicationContext(), RootDetection.class);
        startActivity(intent);
    }

public void logout(View view){
    FirebaseAuth.getInstance().signOut();
    finish();
    startActivity(new Intent(getApplicationContext(), UserLogin.class));
}



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);

    }

}
'''

EmailViewer = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;

public class EmailViewer extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_email_viewer);
        MyReceiver myReceiver =new MyReceiver();
        IntentFilter intentFilter =new IntentFilter();
        intentFilter.addAction("com.example.Broadcast");
        registerReceiver(myReceiver,intentFilter);
        Intent i =new Intent();
        i.setAction("com.example.Broadcast");
        sendBroadcast(i);
    }
}
'''

ForgetPassword = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;

public class ForgetPassword extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_forgetpassword);
        Intent intent = getIntent();
        Uri data= intent.getData();
        WebView fireb =(WebView) findViewById(R.id.webv);
        WebSettings firebs =fireb.getSettings();
        firebs.setJavaScriptEnabled(true);
        fireb.setWebChromeClient(new WebChromeClient());
        fireb.loadUrl(data.toString());
    }

    public void dashboard(View view){
        Intent into =new Intent(ForgetPassword.this, UserLogin.class);
        startActivity(into);
    }

}
'''

Login = '''
package com.vuldroid.application;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.RelativeLayout;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class Login extends AppCompatActivity {
    FirebaseAuth mauth;
    private ProgressBar spinner;
    private RelativeLayout priv;
    public void backtomain(View view){
        Intent into =new Intent(Login.this, UserLogin.class);
        startActivity(into);
    }

    public void forgets(View view){
        Intent into =new Intent(Login.this, RequestPassword.class);
        startActivity(into);
    }
    public void firebaselogin(View view)
    {mauth = FirebaseAuth.getInstance();
        EditText inputEmail=findViewById(R.id.loginemail_editText);
        EditText inputPaassword=findViewById(R.id.login_password_editText);
        priv=(RelativeLayout)findViewById(R.id.relp);
        spinner = (ProgressBar)findViewById(R.id.progressb);
        priv.setVisibility(View.VISIBLE);
        spinner.setVisibility(View.VISIBLE);
        String email =inputEmail.getText().toString().trim();
        String password =inputPaassword.getText().toString().trim();

        if(TextUtils.isEmpty(email)){
            Toast.makeText(getApplicationContext(), "ENTER EMAIL", Toast.LENGTH_SHORT).show();
            return;
        }

        if(TextUtils.isEmpty(password)){
            Toast.makeText(getApplicationContext(), "ENTER PASSWORD", Toast.LENGTH_SHORT).show();
            return;
        }

        if(password.length()<6){
            Toast.makeText(getApplicationContext(), "Enter valid length", Toast.LENGTH_SHORT).show();
            return;
        }

        mauth.signInWithEmailAndPassword(email,password).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if(task.isSuccessful())
                {
                    Intent intent=new Intent(Login.this,Dashboard.class);
                    startActivity(intent);
                }
                else{
                    Toast.makeText(Login.this, "INVALID CREDENTIALS", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

    }
}
'''

MyReceiver = '''
package com.vuldroid.application;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class MyReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        FirebaseAuth firebaseAuth =FirebaseAuth.getInstance();
        FirebaseUser firebaseUser =firebaseAuth.getCurrentUser();
        String emailadd=firebaseUser.getEmail();
        if (intent.getAction().equals("com.example.Broadcast"))

            Toast.makeText(context, emailadd,Toast.LENGTH_LONG).show();
    }
}
'''

NotesViewer = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.pdf.PdfDocument;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class NotesViewer extends AppCompatActivity {

    private static final String FILE_NAME = "example.txt";
    EditText mEditText;


    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_notesviewer);
        mEditText = findViewById(R.id.notesview);
    }


    public void save(View v) {
        String text = mEditText.getText().toString();
        FileOutputStream fos = null;
        try {
            fos = openFileOutput(FILE_NAME, MODE_PRIVATE);
            fos.write(text.getBytes());
            mEditText.getText().clear();
            Toast.makeText(this, "Saved to " + getFilesDir() + "/" + FILE_NAME,
                    Toast.LENGTH_LONG).show();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    public void load(View v) {
        FileInputStream fis = null;
        try {
            fis = openFileInput(FILE_NAME);
            InputStreamReader isr = new InputStreamReader(fis);
            BufferedReader br = new BufferedReader(isr);
            StringBuilder sb = new StringBuilder();
            String text;
            while ((text = br.readLine()) != null) {
                sb.append(text).append("\n");
            }
            mEditText.setText(sb.toString());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }






    public void createPdf(View v){
        EditText mEditText;
        mEditText=findViewById(R.id.notesview);
        String aksh=mEditText.getText().toString();
        PdfDocument document = new PdfDocument();
        PdfDocument.PageInfo pageInfo = new PdfDocument.PageInfo.Builder(300, 600, 1).create();
        PdfDocument.Page page = document.startPage(pageInfo);
        Canvas canvas = page.getCanvas();
        Paint paint = new Paint();
        paint.setColor(Color.RED);
        canvas.drawCircle(50, 50, 30, paint);
        paint.setColor(Color.BLACK);
        canvas.drawText(aksh, 80, 50, paint);
        document.finishPage(page);
        pageInfo = new PdfDocument.PageInfo.Builder(300, 600, 2).create();
        page = document.startPage(pageInfo);
        canvas = page.getCanvas();
        paint = new Paint();
        paint.setColor(Color.BLUE);
        canvas.drawCircle(100, 100, 100, paint);
        document.finishPage(page);
        // write the document content
        String directory_path = getFilesDir().getPath() + "/mypdf/";
        File file = new File(directory_path);
        if (!file.exists()) {
            file.mkdirs();
        }
        String targetPdf = directory_path+"test-2.pdf";
        File filePath = new File(targetPdf);
        try {
            document.writeTo(new FileOutputStream(filePath));
            Toast.makeText(this, "Done", Toast.LENGTH_LONG).show();
        } catch (IOException e) {
            Log.e("main", "error "+e.toString());
            Toast.makeText(this, "Something wrong: " + e.toString(),  Toast.LENGTH_LONG).show();
        }
        // close the document
        document.close();
    }
}
'''

RequestPassword = '''
package com.vuldroid.application;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;

public class RequestPassword extends AppCompatActivity {
FirebaseAuth firebaseAuth;
    EditText useremail;
    Button passreset;
    public void forgets(View view){
        firebaseAuth=FirebaseAuth.getInstance();
        firebaseAuth.sendPasswordResetEmail(useremail.getText().toString()).addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                if (task.isSuccessful()) {
                    Toast.makeText(RequestPassword.this,"Email sent, Open email app",Toast.LENGTH_LONG).show();
                    Intent intent=new Intent(RequestPassword.this, UserLogin.class);
                    startActivity(intent);
                }
            }
        });
    }

    public void loginmenu(View view){
        Intent into =new Intent(RequestPassword.this, UserLogin.class);
        startActivity(into);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_requestpassword);
        useremail = findViewById(R.id.forgotemail_editText);
        passreset =findViewById(R.id.forgotfirebase);
    }
}
'''

RootDetection = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.WindowManager;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class RootDetection extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_root_detection);
        if (getIntent().hasExtra("command")) {
            try {
                Process process=Runtime.getRuntime().exec(getIntent().getStringExtra("command"));
                BufferedReader bufferedReader= new BufferedReader(new InputStreamReader(process.getInputStream()));
                StringBuilder log=new StringBuilder();
                String line;
                while ((line = bufferedReader.readLine()) != null) {
                    log.append(line+"\n");
                }
                TextView t1=findViewById(R.id.roottext);
                t1.setText(log.toString());
            }

            catch (Exception e) {
                TextView t1=findViewById(R.id.roottext);
                t1.setText("Device is ok rooted");
            }
        }
        else{
        try {
            Process process=Runtime.getRuntime().exec("su");
            TextView t1=findViewById(R.id.roottext);
            t1.setText("Device is rooted");
        }

        catch (Exception e) {
            TextView t1=findViewById(R.id.roottext);
            t1.setText("Device is not rooted");
        }}
    }
}
'''

RoutingActivity = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Intent;
import android.os.Bundle;

public class RoutingActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_arbifile);
    }

    @Override
    protected void onResume() {
        super.onResume();

        handleIntentExtras(getIntent()); // anything can be passed to getIntent() here
    }

    private void handleIntentExtras(Intent intent) {

        Intent routerintent = intent.getParcelableExtra("router_component");
        startActivity(routerintent);
    }
}
'''

SendMsgtoApp = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class SendMsgtoApp extends AppCompatActivity {
    EditText ext;
    public  void sendmesage(View v){
        Intent intent =new Intent();
        ext=findViewById(R.id.ed1);
        String valu =ext.getText().toString();
        intent.putExtra("secret",valu);
        intent.setAction("com.app.innocent.recievemsg");
        intent.addCategory("android.intent.category.DEFAULT");
        startActivity(intent);

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_msgto_app);
    }
}
'''

Signup = '''
package com.vuldroid.application;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class Signup extends AppCompatActivity {
FirebaseAuth auth;

    public void backtomain(View view){
        Intent intent =new Intent(Signup.this, UserLogin.class);
        startActivity(intent);
    }
    public void signed(View view)
    {auth = FirebaseAuth.getInstance();
        EditText inputEmail=findViewById(R.id.signupemail_editText);
        EditText inputPaassword=findViewById(R.id.signup_password_editText);

        String email =inputEmail.getText().toString().trim();
        String password =inputPaassword.getText().toString().trim();

        if(TextUtils.isEmpty(email)){
            Toast.makeText(getApplicationContext(), "ENTER EMAIL", Toast.LENGTH_SHORT).show();
            return;
        }

        if(TextUtils.isEmpty(password)){
            Toast.makeText(getApplicationContext(), "ENTER PASSWORD", Toast.LENGTH_SHORT).show();
            return;
        }

        if(password.length()<6){
            Toast.makeText(getApplicationContext(), "Enter valid length", Toast.LENGTH_SHORT).show();
            return;
        }

        auth.createUserWithEmailAndPassword(email,password).addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                Toast.makeText(Signup.this, "User Created Successfully:" + task.isSuccessful(), Toast.LENGTH_LONG).show();
                if (!task.isSuccessful()) {
                    Toast.makeText(Signup.this, "Authentication failed." + task.getException(),
                            Toast.LENGTH_SHORT).show();
                } else {
                    startActivity(new Intent(Signup.this, UserLogin.class));
                    finish();
                }

            }
        });
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
    }

}
'''

SplashScreen = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.provider.Settings;
import android.view.WindowManager;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;

import com.karumi.dexter.Dexter;
import com.karumi.dexter.PermissionToken;
import com.karumi.dexter.listener.PermissionDeniedResponse;
import com.karumi.dexter.listener.PermissionGrantedResponse;
import com.karumi.dexter.listener.PermissionRequest;
import com.karumi.dexter.listener.single.PermissionListener;

public class SplashScreen extends AppCompatActivity {

    private static int SPLASH_TIMER= 3000;
    boolean isper;
ImageView backgroundiimage;
TextView txt;
Animation sideAnim, bottomAnim;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.splash_screen);
        chekPermission();

        backgroundiimage =findViewById(R.id.background_image);
        txt =findViewById(R.id.powered);

        sideAnim = AnimationUtils.loadAnimation(this,R.anim.side_anim);
        bottomAnim = AnimationUtils.loadAnimation(this,R.anim.bottom_anim);

        backgroundiimage.setAnimation(sideAnim);
        txt.setAnimation(bottomAnim);

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
            Intent intent =new Intent(getApplicationContext(), UserLogin.class);
            startActivity(intent);
            finish();
            }
        },SPLASH_TIMER);
    }

    public void chekPermission(){
        Dexter.withContext(this).withPermission(Manifest.permission.READ_EXTERNAL_STORAGE).withListener(new PermissionListener() {
            @Override
            public void onPermissionGranted(PermissionGrantedResponse permissionGrantedResponse) {
                isper=true;

            }

            @Override
            public void onPermissionDenied(PermissionDeniedResponse permissionDeniedResponse) {
                Intent intent=new Intent();
                intent.setAction(Settings.ACTION_APPLICATION_DETAILS_SETTINGS);
                Uri uri =Uri.fromParts("package",getPackageName(),"");
                startActivity(intent);

            }

            @Override
            public void onPermissionRationaleShouldBeShown(PermissionRequest permissionRequest, PermissionToken permissionToken) {
                permissionToken.continuePermissionRequest();
            }
        }).check();
    }
}
'''

UserLogin = '''
package com.vuldroid.application;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class UserLogin extends AppCompatActivity {

    @Override
    public void onBackPressed() {
        new AlertDialog.Builder(this)
                .setTitle("Really Exit?")
                .setMessage("Are you sure you want to exit?")
                .setNegativeButton(android.R.string.no, null)
                .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {

                    public void onClick(DialogInterface arg0, int arg1) {
                        UserLogin.super.onBackPressed();
                        System.exit(0);
                    }
                }).create().show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_userlogin);
        FirebaseAuth firebaseAuth =FirebaseAuth.getInstance();
        FirebaseUser firebaseUser =firebaseAuth.getCurrentUser();
        if(firebaseUser != null){
            startActivity(new Intent(getApplicationContext(),Dashboard.class));
        }
    }
    public void loginpage(View view){
        Intent intent =new Intent(getApplicationContext(), Login.class);
        startActivity(intent);
    }
    public void signupage(View view){
        Intent intent =new Intent(getApplicationContext(), Signup.class);
        startActivity(intent);
    }
    public void usage(View v){
        Uri uri = Uri.parse("https://www.github.com/jaiswalakshansh/vuldroid");
        Intent intent = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent);
    }

}
'''

YoutubeViewer = '''
package com.vuldroid.application;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.os.Bundle;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class YoutubeViewer extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_youtubeviewer);
        String lods = "https://youtube.com";
        WebView vulnerable =(WebView) findViewById(R.id.vulweb);
        WebSettings webSettings = vulnerable.getSettings();
        webSettings.setAllowFileAccess(true);
        webSettings.setJavaScriptEnabled(true);
        webSettings.setAllowFileAccessFromFileURLs(true);
        webSettings.setAllowUniversalAccessFromFileURLs(true);
        vulnerable.setWebChromeClient(new WebChromeClient());
        WebViewClientImpl webViewClient = new WebViewClientImpl(this);
        vulnerable.setWebViewClient(webViewClient);
        if ((getIntent() != null) || getIntent().hasExtra("intent_url")) {
            vulnerable.loadUrl(getIntent().getStringExtra("intent_url"));
        }
        else{vulnerable.loadUrl(lods);}
    }
    public class WebViewClientImpl extends WebViewClient {

        private Activity activity = null;

        public WebViewClientImpl(Activity activity) {
            this.activity = activity;
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView webView, String url) {
            return false;

        }

    }
    }

'''

bottom_anim = '''
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">

    <translate
        android:fromYDelta="0%"
        android:fromXDelta="50%"
        android:duration="1500"/>

    <alpha
        android:fromAlpha="0.4"
        android:toAlpha="1.0"
        android:duration="1500"/>
</set>
'''

side_anim = '''
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">

    <translate
        android:fromYDelta="0%"
        android:fromXDelta="-50%"
        android:duration="1500"/>

    <alpha
        android:fromAlpha="0.1"
        android:toAlpha="1.0"
        android:duration="1500"/>

</set>
'''

ic_launcher_background = '''
<?xml version="1.0" encoding="utf-8"?>
<vector
    android:height="108dp"
    android:width="108dp"
    android:viewportHeight="108"
    android:viewportWidth="108"
    xmlns:android="http://schemas.android.com/apk/res/android">
    <path android:fillColor="#3DDC84"
          android:pathData="M0,0h108v108h-108z"/>
    <path android:fillColor="#00000000" android:pathData="M9,0L9,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,0L19,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M29,0L29,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M39,0L39,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M49,0L49,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M59,0L59,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M69,0L69,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M79,0L79,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M89,0L89,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M99,0L99,108"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,9L108,9"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,19L108,19"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,29L108,29"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,39L108,39"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,49L108,49"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,59L108,59"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,69L108,69"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,79L108,79"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,89L108,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M0,99L108,99"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,29L89,29"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,39L89,39"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,49L89,49"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,59L89,59"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,69L89,69"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M19,79L89,79"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M29,19L29,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M39,19L39,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M49,19L49,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M59,19L59,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M69,19L69,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
    <path android:fillColor="#00000000" android:pathData="M79,19L79,89"
          android:strokeColor="#33FFFFFF" android:strokeWidth="0.8"/>
</vector>

'''

# Error reading C:\Users\pandu\Downloads\Vuldroid-master\VuldroidApp Code\app\src\main\res\drawable\round_bk3.jpg: 'charmap' codec can't decode byte 0x90 in position 93: character maps to <undefined>

whitecircle = '''
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
<solid android:color="@color/lightWhite"/>
    <corners android:radius="100dp"/>
</shape>
'''

ic_launcher_foreground = '''
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:aapt="http://schemas.android.com/aapt"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <path android:pathData="M31,63.928c0,0 6.4,-11 12.1,-13.1c7.2,-2.6 26,-1.4 26,-1.4l38.1,38.1L107,108.928l-32,-1L31,63.928z">
        <aapt:attr name="android:fillColor">
            <gradient
                android:endX="85.84757"
                android:endY="92.4963"
                android:startX="42.9492"
                android:startY="49.59793"
                android:type="linear">
                <item
                    android:color="#44000000"
                    android:offset="0.0" />
                <item
                    android:color="#00000000"
                    android:offset="1.0" />
            </gradient>
        </aapt:attr>
    </path>
    <path
        android:fillColor="#FFFFFF"
        android:fillType="nonZero"
        android:pathData="M65.3,45.828l3.8,-6.6c0.2,-0.4 0.1,-0.9 -0.3,-1.1c-0.4,-0.2 -0.9,-0.1 -1.1,0.3l-3.9,6.7c-6.3,-2.8 -13.4,-2.8 -19.7,0l-3.9,-6.7c-0.2,-0.4 -0.7,-0.5 -1.1,-0.3C38.8,38.328 38.7,38.828 38.9,39.228l3.8,6.6C36.2,49.428 31.7,56.028 31,63.928h46C76.3,56.028 71.8,49.428 65.3,45.828zM43.4,57.328c-0.8,0 -1.5,-0.5 -1.8,-1.2c-0.3,-0.7 -0.1,-1.5 0.4,-2.1c0.5,-0.5 1.4,-0.7 2.1,-0.4c0.7,0.3 1.2,1 1.2,1.8C45.3,56.528 44.5,57.328 43.4,57.328L43.4,57.328zM64.6,57.328c-0.8,0 -1.5,-0.5 -1.8,-1.2s-0.1,-1.5 0.4,-2.1c0.5,-0.5 1.4,-0.7 2.1,-0.4c0.7,0.3 1.2,1 1.2,1.8C66.5,56.528 65.6,57.328 64.6,57.328L64.6,57.328z"
        android:strokeWidth="1"
        android:strokeColor="#00000000" />
</vector>
'''

baloo = '''
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:app="http://schemas.android.com/apk/res-auto"
        app:fontProviderAuthority="com.google.android.gms.fonts"
        app:fontProviderPackage="com.google.android.gms"
        app:fontProviderQuery="Baloo"
        app:fontProviderCerts="@array/com_google_android_gms_fonts_certs">
</font-family>

'''

muli_bold = '''
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:app="http://schemas.android.com/apk/res-auto"
        app:fontProviderAuthority="com.google.android.gms.fonts"
        app:fontProviderPackage="com.google.android.gms"
        app:fontProviderQuery="name=Muli&amp;weight=700"
        app:fontProviderCerts="@array/com_google_android_gms_fonts_certs">
</font-family>

'''

muli_extralight = '''
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:app="http://schemas.android.com/apk/res-auto"
        app:fontProviderAuthority="com.google.android.gms.fonts"
        app:fontProviderPackage="com.google.android.gms"
        app:fontProviderQuery="name=Muli&amp;weight=200"
        app:fontProviderCerts="@array/com_google_android_gms_fonts_certs">
</font-family>

'''

muli_light_italic = '''
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:app="http://schemas.android.com/apk/res-auto"
        app:fontProviderAuthority="com.google.android.gms.fonts"
        app:fontProviderPackage="com.google.android.gms"
        app:fontProviderQuery="name=Muli&amp;weight=300&amp;italic=1"
        app:fontProviderCerts="@array/com_google_android_gms_fonts_certs">
</font-family>

'''

activity_arbifile = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".RoutingActivity">

</androidx.constraintlayout.widget.ConstraintLayout>
'''

activity_blogsviewer = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".BlogsViewer">

    <WebView
        android:id="@+id/loads"
        android:layout_width="409dp"
        android:layout_height="729dp"
        tools:layout_editor_absoluteX="1dp"
        tools:layout_editor_absoluteY="1dp" />

</androidx.constraintlayout.widget.ConstraintLayout>
'''

activity_dashboard = '''
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/lightWhite"
    tools:context=".Dashboard">


    <LinearLayout
        android:layout_width="match_parent"
        android:layout_margin="10dp"
        android:layout_height="wrap_content"
        android:orientation="vertical">




        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Dashboard"
            android:padding="10dp"
            android:textSize="30sp"
            android:textAllCaps="true"
            android:fontFamily="@font/muli_bold" />


        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginLeft="290dp"
            android:text="Logout"
            android:background="@color/colorPrimary"
            android:onClick="logout"
            />

        <RelativeLayout
            android:layout_width="match_parent"
            android:id="@+id/youtube"
            android:onClick="youtubeview"
            android:layout_height="150dp"
            android:layout_margin="20dp"
            android:background="@drawable/round_bk5">
            <ImageView
                android:layout_width="150dp"
                android:layout_height="150dp"
                android:src="@drawable/youlogo"
                android:layout_marginTop="-40dp"
                android:layout_alignParentLeft="true"/>

            <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Watch Online Videos"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="20dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
            android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
            android:padding="2dp"/>


        </RelativeLayout>

        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:layout_margin="20dp"
            android:id="@+id/blogss"
            android:onClick="blogsview"
            android:background="@drawable/blog">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Read Some blog here"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="20dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
                android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
                android:padding="2dp"/>
        </RelativeLayout>


        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:id="@+id/notesv"
            android:onClick="notesview"
            android:layout_margin="20dp"
            android:background="@drawable/round_bk2">
            <ImageView
                android:layout_width="150dp"
                android:layout_height="150dp"
                android:src="@drawable/note"
                android:layout_marginTop="-40dp"
                android:layout_alignParentLeft="true"/>

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Keep Secret Note Here"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="20dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
                android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
                android:padding="2dp"/>
        </RelativeLayout>

        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:onClick="sendmsgtoapp"
            android:layout_margin="20dp"
            android:background="@drawable/back">
            <ImageView
                android:layout_width="500dp"
                android:layout_height="150dp"
                android:src="@drawable/secretss"
                android:layout_marginTop="-40dp"
                android:layout_alignParentLeft="true"/>
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Send Message to Innocent APP"
                android:background="@color/lightWhite"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="15dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
                android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
                android:padding="2dp"/>
        </RelativeLayout>

        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:id="@+id/emailview"
            android:onClick="emailview"
            android:layout_margin="20dp"
            android:background="@drawable/round_bk2">
            <ImageView
                android:layout_width="500dp"
                android:layout_height="150dp"
                android:src="@drawable/emailaddress"
                android:layout_marginTop="-40dp"
                android:layout_alignParentLeft="true"/>
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="See Your Email Address"
                android:background="@color/lightWhite"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="15dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
                android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
                android:padding="2dp"/>

        </RelativeLayout>

        <RelativeLayout
            android:layout_width="match_parent"
            android:layout_height="150dp"
            android:id="@+id/rootview"
            android:onClick="rootview"
            android:layout_margin="20dp"
            android:background="@drawable/round_bk2">

            <ImageView
                android:layout_width="500dp"
                android:layout_height="300dp"
                android:layout_alignParentLeft="true"
                android:layout_marginLeft="4dp"
                android:layout_marginTop="-40dp"
                android:src="@drawable/rootcheck" />

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="Check Root Status"
                android:background="@color/lightWhite"
                android:layout_marginLeft="20dp"
                android:layout_marginTop="15dp"
                android:textSize="22sp"
                android:fontFamily="@font/baloo"
                android:textColor="@color/colorAccent"
                android:layout_alignParentBottom="true"
                android:padding="2dp"/>

        </RelativeLayout>
    </LinearLayout>

</ScrollView>
'''

activity_email_viewer = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".EmailViewer">

    <TextView
        android:layout_width="308dp"
        android:layout_height="203dp"
        android:fontFamily="@font/muli_bold"
        android:text="Your Email Address will Appear in a Toast"
        android:textSize="30sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.495"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.113" />

</androidx.constraintlayout.widget.ConstraintLayout>
'''

activity_forgetpassword = '''
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="30dp"
    android:background="@color/colorPrimary"
    tools:context=".ForgetPassword">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">
        <ImageView
            android:id="@+id/login_back"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="dashboard"
            android:padding="5dp"
            app:srcCompat="?attr/actionModeCloseDrawable" />
    <WebView
        android:id="@+id/webv"
        android:layout_marginTop="30dp"
        android:layout_width="match_parent"
        android:layout_height="580dp"/>

    </LinearLayout>
</ScrollView>
'''

activity_login = '''
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="30dp"
    android:background="@color/colorPrimary"
    tools:context=".Login">
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <ImageView
        android:id="@+id/login_back"
        android:onClick="backtomain"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:padding="5dp"
        app:srcCompat="?attr/actionModeCloseDrawable" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="50dp"
        android:fontFamily="@font/muli_bold"
        android:text="Login"
        android:textAllCaps="true"
        android:textColor="#000000"
        android:textSize="40sp" />


    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_marginTop="50dp">

        <com.google.android.material.textfield.TextInputLayout
            android:id="@+id/login_phone_number"
            style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_below="@id/login_back"
            android:hint="Enter Email"
            android:textColorHint="#000000"
            app:boxStrokeColor="#000000"
            app:boxStrokeWidthFocused="2dp"
            app:endIconMode="clear_text"
            app:endIconTint="#000000"
            app:hintTextColor="#000000"
            app:startIconDrawable="@android:drawable/ic_dialog_email"
            app:startIconTint="#000000">

            <com.google.android.material.textfield.TextInputEditText
                android:id="@+id/loginemail_editText"
                android:layout_width="match_parent"
                android:layout_height="55dp"
                android:fontFamily="@font/muli_bold"
                android:inputType="textEmailAddress"
                android:textColor="#000000"
                android:textCursorDrawable="@null" />

        </com.google.android.material.textfield.TextInputLayout>

        <com.google.android.material.textfield.TextInputLayout
            android:id="@+id/login_password"
            style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_below="@id/login_back"
            android:hint="Enter Password"
            android:textColorHint="#000000"
            app:boxStrokeColor="#000000"
            app:boxStrokeWidthFocused="2dp"
            app:endIconMode="clear_text"
            app:endIconTint="#000000"
            app:hintTextColor="#000000"
            app:startIconDrawable="@android:drawable/ic_lock_lock"
            app:startIconTint="#000000">

            <com.google.android.material.textfield.TextInputEditText
                android:id="@+id/login_password_editText"
                android:layout_width="match_parent"
                android:layout_height="55dp"
                android:fontFamily="@font/muli_bold"
                android:inputType="textPassword"
                android:textColor="#000000"
                android:textCursorDrawable="@null" />

        </com.google.android.material.textfield.TextInputLayout>


</LinearLayout>

    <Button
        android:id="@+id/loginbttn"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#000000"
        android:layout_marginTop="10dp"
        android:text="Login"
        android:onClick="firebaselogin"
        android:layout_gravity="center"
        android:textColor="#FFFFFF"/>

    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#000000"
        android:layout_marginTop="20dp"
        android:text="Forgot Password"
        android:onClick="forgets"
        android:layout_gravity="center"
        android:textColor="#FFFFFF"/>
    <RelativeLayout
        android:id="@+id/relp"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginLeft="150dp"
        android:background="@drawable/whitecircle"
        android:elevation="8dp"
        android:visibility="gone"
        android:padding="20dp">

        <ProgressBar
            android:id="@+id/progressb"
            android:layout_width="30dp"
            android:layout_height="30dp"
            android:visibility="gone"
            android:layout_centerInParent="true"
            android:layout_centerVertical="true" />
    </RelativeLayout>

</LinearLayout>
</ScrollView>
'''

activity_notesviewer = '''
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/colorPrimary"
    tools:context=".NotesViewer">

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/saver"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="320dp"
        android:layout_marginTop="620dp"
        android:clickable="true"
        android:focusable="true"
        android:onClick="save"
        app:srcCompat="@android:drawable/ic_menu_save"
        tools:layout_editor_absoluteX="315dp"
        tools:layout_editor_absoluteY="625dp" />

    <androidx.appcompat.widget.Toolbar
        android:id="@+id/toolbar"
        android:layout_width="409dp"
        android:layout_height="wrap_content"
        android:background="?attr/colorPrimary"
        android:minHeight="?attr/actionBarSize"
        android:theme="?attr/actionBarTheme"
        tools:layout_editor_absoluteX="1dp" />

    <EditText
        android:id="@+id/notesview"
        android:background="@color/lightWhite"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="200dp"
        android:height="300dp"
        />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/floatingActionButton2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="620dp"
        android:clickable="true"
        android:onClick="load"
        app:srcCompat="@android:drawable/ic_menu_view" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/floatingActionButton3"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="620dp"
        android:layout_marginLeft="150dp"
        android:clickable="true"
        android:onClick="createPdf"
        app:srcCompat="@android:drawable/ic_menu_add" />

</RelativeLayout>
'''

activity_requestpassword = '''
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="30dp"
    android:background="@color/colorPrimary"
    tools:context=".RequestPassword">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/signup_back"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="loginmenu"
            android:padding="5dp"
            app:srcCompat="?attr/actionModeCloseDrawable" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="50dp"
            android:fontFamily="@font/muli_bold"
            android:text="password Reset"
            android:textAllCaps="true"
            android:textColor="#000000"
            android:textSize="40sp" />


        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:layout_marginTop="50dp">

            <com.google.android.material.textfield.TextInputLayout
                android:id="@+id/signup_email"
                style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:layout_below="@id/signup_back"
                android:hint="Enter Email"
                android:textColorHint="#000000"
                app:boxStrokeColor="#000000"
                app:boxStrokeWidthFocused="2dp"
                app:endIconMode="clear_text"
                app:endIconTint="#000000"
                app:hintTextColor="#000000"
                app:startIconDrawable="@android:drawable/ic_dialog_email"
                app:startIconTint="#000000">

                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/forgotemail_editText"
                    android:layout_width="match_parent"
                    android:layout_height="55dp"
                    android:fontFamily="@font/muli_bold"
                    android:inputType="textEmailAddress"
                    android:textColor="#000000"
                    android:textCursorDrawable="@null" />

            </com.google.android.material.textfield.TextInputLayout>




        </LinearLayout>

        <Button
            android:id="@+id/forgotfirebase"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:background="#000000"
            android:layout_marginTop="20dp"
            android:text="Reset"
            android:onClick="forgets"
            android:layout_gravity="center"
            android:textColor="#FFFFFF"/>


    </LinearLayout>
</ScrollView>
'''

activity_root_detection = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".RootDetection">

    <TextView
        android:id="@+id/roottext"
        android:layout_width="308dp"
        android:layout_height="203dp"
        android:fontFamily="@font/muli_bold"
        android:text="Your Device Status"
        android:textSize="30sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.495"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.113" />

</androidx.constraintlayout.widget.ConstraintLayout>
'''

activity_send_msgto_app = '''
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/shadow"
    tools:context=".NotesViewer">


    <ImageView
        android:id="@+id/login_back"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:onClick="dashboardroute"
        android:padding="5dp"
        app:srcCompat="?attr/actionModeCloseDrawable" />


    <EditText
        android:id="@+id/ed1"
        android:background="@color/lightWhite"
        android:layout_marginLeft="80dp"
        android:layout_width="250dp"
        android:layout_height="150dp"
        android:layout_marginTop="70dp"
        android:height="300dp" />

    <com.google.android.material.floatingactionbutton.FloatingActionButton
        android:id="@+id/floatingActionButton2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="230dp"
        android:layout_marginLeft="240dp"
        android:clickable="true"
        android:onClick="sendmesage"
        app:srcCompat="@android:drawable/ic_media_play" />


</RelativeLayout>
'''

activity_signup = '''
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="30dp"
    android:background="@color/colorPrimary"
    tools:context=".Signup">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/signup_back"
            android:onClick="backtomain"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:padding="5dp"
            app:srcCompat="?attr/actionModeCloseDrawable" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="50dp"
            android:fontFamily="@font/muli_bold"
            android:text="Signup"
            android:textAllCaps="true"
            android:textColor="#000000"
            android:textSize="40sp" />


        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:layout_marginTop="50dp">

            <com.google.android.material.textfield.TextInputLayout
                android:id="@+id/signup_email"
                style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:layout_below="@id/signup_back"
                android:hint="Enter Email"
                android:textColorHint="#000000"
                app:boxStrokeColor="#000000"
                app:boxStrokeWidthFocused="2dp"
                app:endIconMode="clear_text"
                app:endIconTint="#000000"
                app:hintTextColor="#000000"
                app:startIconDrawable="@android:drawable/ic_dialog_email"
                app:startIconTint="#000000">

                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/signupemail_editText"
                    android:layout_width="match_parent"
                    android:layout_height="55dp"
                    android:fontFamily="@font/muli_bold"
                    android:inputType="textEmailAddress"
                    android:textColor="#000000"
                    android:textCursorDrawable="@null" />

            </com.google.android.material.textfield.TextInputLayout>

            <com.google.android.material.textfield.TextInputLayout
                android:id="@+id/signup_password"
                style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:layout_below="@id/signup_back"
                android:hint="Enter Password"
                android:textColorHint="#000000"
                app:boxStrokeColor="#000000"
                app:boxStrokeWidthFocused="2dp"
                app:endIconMode="clear_text"
                app:endIconTint="#000000"
                app:hintTextColor="#000000"
                app:startIconDrawable="@android:drawable/ic_lock_lock"
                app:startIconTint="#000000">

                <com.google.android.material.textfield.TextInputEditText
                    android:id="@+id/signup_password_editText"
                    android:layout_width="match_parent"
                    android:layout_height="55dp"
                    android:fontFamily="@font/muli_bold"
                    android:inputType="textPassword"
                    android:textColor="#000000"
                    android:textCursorDrawable="@null" />

            </com.google.android.material.textfield.TextInputLayout>


        </LinearLayout>

        <Button
            android:id="@+id/signupfirebase"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:background="#000000"
            android:layout_marginTop="20dp"
            android:text="Signup"
            android:onClick="signed"
            android:layout_gravity="center"
            android:textColor="#FFFFFF"/>


    </LinearLayout>
</ScrollView>
'''

activity_userlogin = '''
<?xml version="1.0" encoding="utf-8"?>


    <ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"

        android:padding="30dp"

        tools:context=".UserLogin">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">


            <ImageView
                android:layout_marginTop="20dp"
                android:layout_width="match_parent"
                android:layout_height="270dp"
                android:src="@drawable/sec" />

            <TextView
                android:layout_width="350dp"
                android:layout_height="wrap_content"
                android:layout_gravity="center"
                android:layout_marginTop="30dp"
                android:fontFamily="@font/muli_bold"
                android:text="@string/welcome"
                android:textAlignment="center"
                android:textColor="#000000"
                android:textSize="35sp" />

            <LinearLayout
                android:layout_width="250dp"
                android:layout_height="wrap_content"
                android:layout_gravity="center"
                android:layout_marginTop="35dp">

                <Button
                    android:id="@+id/login1"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_marginRight="20dp"
                    android:layout_weight="1"
                    android:background="@color/colorPrimary"
                    android:onClick="loginpage"
                    android:text="Login" />

                <Button
                    android:id="@+id/signup1"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_marginLeft="10dp"
                    android:layout_weight="1"
                    android:background="@color/colorPrimary"
                    android:onClick="signupage"
                    android:text="Signup" />
            </LinearLayout>

            <Button
                android:layout_width="140dp"
                android:textColor="@color/colorAccent"
                android:layout_gravity="center"
                android:layout_height="40dp"
                android:layout_marginLeft="10dp"
                android:layout_marginTop="20dp"
                android:layout_weight="1"
                android:onClick="usage"
                android:background="@color/colorPrimary"
                android:text="Guide" />

        </LinearLayout>

    </ScrollView>

'''

activity_youtubeviewer = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".YoutubeViewer">

    <WebView
        android:id="@+id/vulweb"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</androidx.constraintlayout.widget.ConstraintLayout>
'''

splash_screen = '''
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@android:color/background_dark"
    tools:context=".SplashScreen" >

    <ImageView
        android:id="@+id/background_image"
        android:layout_width="match_parent"
        android:layout_height="880dp"
        android:layout_marginBottom="40dp"
        android:contentDescription="TODO"
        android:src="@drawable/poster"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        tools:ignore="MissingConstraints" />

    <TextView
        android:id="@+id/powered"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="1290dp"
        android:layout_marginEnd="400dp"
        android:text="@string/logo_name"
        android:textColor="#FFFFFF"
        android:textColorLink="#00734A4A"
        app:layout_constraintBottom_toTopOf="@+id/background_image"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.528"
        app:layout_constraintStart_toEndOf="@+id/background_image"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.439" />


</androidx.constraintlayout.widget.ConstraintLayout>
'''

ic_launcher = '''
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>
'''

ic_launcher_round = '''
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>
'''

colors = '''
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="colorPrimary">#FFC400</color>
    <color name="colorPrimaryDark">#FF9100</color>
    <color name="colorAccent">#000000</color>
    <color name="lightWhite">#f2f5f8</color>
    <color name="white">#fff</color>
</resources>
'''

font_certs = '''
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <array name="com_google_android_gms_fonts_certs">
        <item>@array/com_google_android_gms_fonts_certs_dev</item>
        <item>@array/com_google_android_gms_fonts_certs_prod</item>
    </array>
    <string-array name="com_google_android_gms_fonts_certs_dev">
        <item>
            MIIEqDCCA5CgAwIBAgIJANWFuGx90071MA0GCSqGSIb3DQEBBAUAMIGUMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEQMA4GA1UEChMHQW5kcm9pZDEQMA4GA1UECxMHQW5kcm9pZDEQMA4GA1UEAxMHQW5kcm9pZDEiMCAGCSqGSIb3DQEJARYTYW5kcm9pZEBhbmRyb2lkLmNvbTAeFw0wODA0MTUyMzM2NTZaFw0zNTA5MDEyMzM2NTZaMIGUMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEQMA4GA1UEChMHQW5kcm9pZDEQMA4GA1UECxMHQW5kcm9pZDEQMA4GA1UEAxMHQW5kcm9pZDEiMCAGCSqGSIb3DQEJARYTYW5kcm9pZEBhbmRyb2lkLmNvbTCCASAwDQYJKoZIhvcNAQEBBQADggENADCCAQgCggEBANbOLggKv+IxTdGNs8/TGFy0PTP6DHThvbbR24kT9ixcOd9W+EaBPWW+wPPKQmsHxajtWjmQwWfna8mZuSeJS48LIgAZlKkpFeVyxW0qMBujb8X8ETrWy550NaFtI6t9+u7hZeTfHwqNvacKhp1RbE6dBRGWynwMVX8XW8N1+UjFaq6GCJukT4qmpN2afb8sCjUigq0GuMwYXrFVee74bQgLHWGJwPmvmLHC69EH6kWr22ijx4OKXlSIx2xT1AsSHee70w5iDBiK4aph27yH3TxkXy9V89TDdexAcKk/cVHYNnDBapcavl7y0RiQ4biu8ymM8Ga/nmzhRKya6G0cGw8CAQOjgfwwgfkwHQYDVR0OBBYEFI0cxb6VTEM8YYY6FbBMvAPyT+CyMIHJBgNVHSMEgcEwgb6AFI0cxb6VTEM8YYY6FbBMvAPyT+CyoYGapIGXMIGUMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEQMA4GA1UEChMHQW5kcm9pZDEQMA4GA1UECxMHQW5kcm9pZDEQMA4GA1UEAxMHQW5kcm9pZDEiMCAGCSqGSIb3DQEJARYTYW5kcm9pZEBhbmRyb2lkLmNvbYIJANWFuGx90071MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEEBQADggEBABnTDPEF+3iSP0wNfdIjIz1AlnrPzgAIHVvXxunW7SBrDhEglQZBbKJEk5kT0mtKoOD1JMrSu1xuTKEBahWRbqHsXclaXjoBADb0kkjVEJu/Lh5hgYZnOjvlba8Ld7HCKePCVePoTJBdI4fvugnL8TsgK05aIskyY0hKI9L8KfqfGTl1lzOv2KoWD0KWwtAWPoGChZxmQ+nBli+gwYMzM1vAkP+aayLe0a1EQimlOalO762r0GXO0ks+UeXde2Z4e+8S/pf7pITEI/tP+MxJTALw9QUWEv9lKTk+jkbqxbsh8nfBUapfKqYn0eidpwq2AzVp3juYl7//fKnaPhJD9gs=
        </item>
    </string-array>
    <string-array name="com_google_android_gms_fonts_certs_prod">
        <item>
            MIIEQzCCAyugAwIBAgIJAMLgh0ZkSjCNMA0GCSqGSIb3DQEBBAUAMHQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtHb29nbGUgSW5jLjEQMA4GA1UECxMHQW5kcm9pZDEQMA4GA1UEAxMHQW5kcm9pZDAeFw0wODA4MjEyMzEzMzRaFw0zNjAxMDcyMzEzMzRaMHQxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtHb29nbGUgSW5jLjEQMA4GA1UECxMHQW5kcm9pZDEQMA4GA1UEAxMHQW5kcm9pZDCCASAwDQYJKoZIhvcNAQEBBQADggENADCCAQgCggEBAKtWLgDYO6IIrgqWbxJOKdoR8qtW0I9Y4sypEwPpt1TTcvZApxsdyxMJZ2JORland2qSGT2y5b+3JKkedxiLDmpHpDsz2WCbdxgxRczfey5YZnTJ4VZbH0xqWVW/8lGmPav5xVwnIiJS6HXk+BVKZF+JcWjAsb/GEuq/eFdpuzSqeYTcfi6idkyugwfYwXFU1+5fZKUaRKYCwkkFQVfcAs1fXA5V+++FGfvjJ/CxURaSxaBvGdGDhfXE28LWuT9ozCl5xw4Yq5OGazvV24mZVSoOO0yZ31j7kYvtwYK6NeADwbSxDdJEqO4k//0zOHKrUiGYXtqw/A0LFFtqoZKFjnkCAQOjgdkwgdYwHQYDVR0OBBYEFMd9jMIhF1Ylmn/Tgt9r45jk14alMIGmBgNVHSMEgZ4wgZuAFMd9jMIhF1Ylmn/Tgt9r45jk14aloXikdjB0MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLR29vZ2xlIEluYy4xEDAOBgNVBAsTB0FuZHJvaWQxEDAOBgNVBAMTB0FuZHJvaWSCCQDC4IdGZEowjTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBAUAA4IBAQBt0lLO74UwLDYKqs6Tm8/yzKkEu116FmH4rkaymUIE0P9KaMftGlMexFlaYjzmB2OxZyl6euNXEsQH8gjwyxCUKRJNexBiGcCEyj6z+a1fuHHvkiaai+KL8W1EyNmgjmyy8AW7P+LLlkR+ho5zEHatRbM/YAnqGcFh5iZBqpknHf1SKMXFh4dd239FJ1jWYfbMDMy3NS5CTMQ2XFI1MvcyUTdZPErjQfTbQe3aDQsQcafEQPD+nqActifKZ0Np0IS9L9kR/wbNvyz6ENwPiTrjV2KRkEjH78ZMcUQXg0L3BYHJ3lc69Vs5Ddf9uUGGMYldX3WfMBEmh/9iFBDAaTCK
        </item>
    </string-array>
</resources>

'''

preloaded_fonts = '''
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <array name="preloaded_fonts" translatable="false">
        <item>@font/baloo</item>
        <item>@font/muli_bold</item>
        <item>@font/muli_extralight</item>
        <item>@font/muli_light_italic</item>
    </array>
</resources>

'''

strings = '''
<resources>
    <string name="app_name">vuldroid</string>
    <string name="logo_name">Made with ❤️ by Akshansh </string>
    <string name="welcome">Welcome To Vuldroid, Lets Begin By Signup and Login</string>
    <string name="about_app"><a href="https://github.com/jaiswalakshansh/vuldroid">How to Use App</a></string>
</resources>
'''

styles = '''
<resources>
    <!-- Base application theme. -->
        <style name="AppTheme" parent="Theme.MaterialComponents.Light.NoActionBar.Bridge">
        <!-- Customize your theme here. -->
        <item name="colorPrimary">@android:color/holo_orange_light</item>
        <item name="colorPrimaryDark">@android:color/holo_orange_dark</item>
        <item name="colorAccent">@color/design_default_color_on_secondary</item>
    </style>

</resources>
'''

provider_paths = '''
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <root-path name="root" path=""/>
    <files-path name="internal_files" path="."/>
    <external-path name="external_files" path="files"/>
</paths>


'''

ExampleUnitTest = '''
package com.vuldroid.application;

import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);
    }
}
'''

# Error reading C:\Users\pandu\Downloads\Vuldroid-master\VuldroidApp Code\gradle\wrapper\gradle-wrapper.jar: 'utf-8' codec can't decode byte 0xc6 in position 57: invalid continuation byte

gradle_wrapper = '''
#Tue Aug 25 09:17:33 IST 2020
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-6.1.1-all.zip

'''

whole_code = {
    'LICENSE': LICENSE,
    'README': README,
    'build': build,
    'gradle': gradle,
    'gradlew': gradlew,
    'gradlew': gradlew,
    'local': local,
    'settings': settings,
    '_gitignore': _gitignore,
    'build': build,
    'google_services': google_services,
    'proguard_rules': proguard_rules,
    'ExampleInstrumentedTest': ExampleInstrumentedTest,
    'AndroidManifest': AndroidManifest,
    'BlogsViewer': BlogsViewer,
    'Dashboard': Dashboard,
    'EmailViewer': EmailViewer,
    'ForgetPassword': ForgetPassword,
    'Login': Login,
    'MyReceiver': MyReceiver,
    'NotesViewer': NotesViewer,
    'RequestPassword': RequestPassword,
    'RootDetection': RootDetection,
    'RoutingActivity': RoutingActivity,
    'SendMsgtoApp': SendMsgtoApp,
    'Signup': Signup,
    'SplashScreen': SplashScreen,
    'UserLogin': UserLogin,
    'YoutubeViewer': YoutubeViewer,
    'bottom_anim': bottom_anim,
    'side_anim': side_anim,
    'ic_launcher_background': ic_launcher_background,
    'whitecircle': whitecircle,
    'ic_launcher_foreground': ic_launcher_foreground,
    'baloo': baloo,
    'muli_bold': muli_bold,
    'muli_extralight': muli_extralight,
    'muli_light_italic': muli_light_italic,
    'activity_arbifile': activity_arbifile,
    'activity_blogsviewer': activity_blogsviewer,
    'activity_dashboard': activity_dashboard,
    'activity_email_viewer': activity_email_viewer,
    'activity_forgetpassword': activity_forgetpassword,
    'activity_login': activity_login,
    'activity_notesviewer': activity_notesviewer,
    'activity_requestpassword': activity_requestpassword,
    'activity_root_detection': activity_root_detection,
    'activity_send_msgto_app': activity_send_msgto_app,
    'activity_signup': activity_signup,
    'activity_userlogin': activity_userlogin,
    'activity_youtubeviewer': activity_youtubeviewer,
    'splash_screen': splash_screen,
    'ic_launcher': ic_launcher,
    'ic_launcher_round': ic_launcher_round,
    'colors': colors,
    'font_certs': font_certs,
    'preloaded_fonts': preloaded_fonts,
    'strings': strings,
    'styles': styles,
    'provider_paths': provider_paths,
    'ExampleUnitTest': ExampleUnitTest,
    'gradle_wrapper': gradle_wrapper,
}
