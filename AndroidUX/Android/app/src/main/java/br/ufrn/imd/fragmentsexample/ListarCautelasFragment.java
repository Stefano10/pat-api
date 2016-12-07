package br.ufrn.imd.fragmentsexample;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;


import static br.ufrn.imd.fragmentsexample.R.id.cautelasBT;


public class ListarCautelasFragment extends Fragment {

    TextView teste;
    Button cautelasBT;
    String URL = "http://159.203.75.66/pat/cautelas";
    //String url ="http://compras.dados.gov.br/fornecedores/v1/fornecedores.json?uf=PB";

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View v = inflater.inflate(R.layout.fragment_listar_cautelas, container, false);
        teste = (TextView) v.findViewById(R.id.testeAPI);
        cautelasBT = (Button) v.findViewById(R.id.cautelasBT);


        cautelasBT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                RequestQueue queue = Volley.newRequestQueue(getContext());


// Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.GET, URL,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                // Display the first 500 characters of the response string.
                                teste.setText("Response is: "+ response);
                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        teste.setText("That didn't work!");
                    }
                });
// Add the request to the RequestQueue.
                queue.add(stringRequest);

            }
        });

        return v;

    }



}
