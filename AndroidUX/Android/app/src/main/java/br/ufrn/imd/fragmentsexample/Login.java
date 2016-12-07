package br.ufrn.imd.fragmentsexample;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class Login extends AppCompatActivity {

    private EditText login, senha;

   

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        login = (EditText) findViewById(R.id.senhaID);
        senha = (EditText) findViewById(R.id.senhaID);
    }

    public void logar( View v){

        String login1 = login.getText().toString();
        String senha1 = senha.getText().toString();

        if (verificar(login1, senha1)) {

            Intent i = new Intent(this, MainActivity.class);
            startActivity(i);
        }



    }

    public boolean verificar(String login, String senha){

        return true;
    }

}
