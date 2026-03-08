// Path: automatax1/app/src/main/java/com/automatax1/MainActivity.kt
package com.automatax1

import android.content.Intent
import android.os.Bundle
import android.provider.Settings
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    
    private lateinit var statusText: TextView
    private lateinit var btnOpenEditor: Button
    private lateinit var btnSettings: Button
    private lateinit var btnCheckPermission: Button
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        statusText = findViewById(R.id.statusText)
        btnOpenEditor = findViewById(R.id.btnOpenEditor)
        btnSettings = findViewById(R.id.btnSettings)
        btnCheckPermission = findViewById(R.id.btnCheckPermission)
        
        btnOpenEditor.setOnClickListener {
            startActivity(Intent(this, ScriptEditorActivity::class.java))
        }
        
        btnSettings.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
        }
        
        btnCheckPermission.setOnClickListener {
            checkAccessibilityPermission()
        }
        
        updateStatus()
    }
    
    private fun checkAccessibilityPermission() {
        val enabled = isAccessibilityServiceEnabled()
        if (!enabled) {
            Toast.makeText(this, "Please enable automatax1 in Accessibility Settings", Toast.LENGTH_LONG).show()
            startActivity(Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS))
        } else {
            Toast.makeText(this, "✅ Accessibility is enabled!", Toast.LENGTH_SHORT).show()
        }
        updateStatus()
    }
    
    private fun isAccessibilityServiceEnabled(): Boolean {
        val enabledServices = Settings.Secure.getString(
            contentResolver,
            Settings.Secure.ENABLED_ACCESSIBILITY_SERVICES
        ) ?: return false
        
        return enabledServices.contains(packageName)
    }
    
    private fun updateStatus() {
        val enabled = isAccessibilityServiceEnabled()
        statusText.text = if (enabled) {
            "✅ Accessibility: Enabled"
        } else {
            "❌ Accessibility: Disabled"
        }
    }
}