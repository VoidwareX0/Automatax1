package com.example.testapp;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.EditText;

public class MainActivity extends Activity {

    Button btn;
    TextView output;
    EditText input;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn = findViewById(R.id.btnClick);
        output = findViewById(R.id.outputText);
        input = findViewById(R.id.inputText);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String text = input.getText().toString();

                if(text.isEmpty()){
                    output.setText("Type something first ⚠️");
                } else {
                    output.setText("You typed: " + text);
                }

            }
        });
    }
}