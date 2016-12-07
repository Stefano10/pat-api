package br.ufrn.imd.fragmentsexample;

import android.os.Bundle;
import android.support.v4.app.Fragment;

import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class LoginFragment extends Fragment {


    String url = "http://159.203.75.66/pat/login";
    Button logarBtn;
    EditText login;
    EditText senha;
    TextView testeLogin;




    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View v = inflater.inflate(R.layout.fragment_login, container, false);

        logarBtn = (Button) v.findViewById(R.id.logarBtn);
        login = (EditText) v.findViewById(R.id.loginID);
        senha = (EditText) v.findViewById(R.id.senhaID);



        logarBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                RequestQueue queue = Volley.newRequestQueue(getContext());

// POST parameters
                Map<String, String> params = new HashMap<String, String>();
                params.put("login", login.getText().toString());
                params.put("senha", senha.getText().toString());


                JSONObject jsonObj = new JSONObject(params);

// Request a json response from the provided URL
                JsonObjectRequest jsonObjRequest = new JsonObjectRequest
                        (Request.Method.POST, url, jsonObj, new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {

                                if(response.toString().contains("TRUE")){
                                    FragmentTransaction ft = getActivity().getSupportFragmentManager().beginTransaction();
                                    ft.replace(R.id.content_main, new BuscaFragment());
                                    ft.addToBackStack(null);
                                    ft.commit();

                                }
                                else{
                                    Toast.makeText(getContext(), "Usuario ou Senha Incorreta", Toast.LENGTH_SHORT).show();
                                }

                            }
                        },
                                new Response.ErrorListener() {
                                    @Override
                                    public void onErrorResponse(VolleyError error) {
                                        Toast.makeText(getContext(), error.toString(), Toast.LENGTH_SHORT).show();
                                    }
                                });

// Add the request to the RequestQueue.
                queue.add(jsonObjRequest);



            }



        });



        return v;
    }


}
