package br.ufrn.imd.fragmentsexample;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;


public class ProtocoloFragment extends Fragment {

    Button cadastrarProtBT;
    EditText origem;
    EditText destino;
    EditText idObjeto;
    String data;
    int dia;
    int mes;
    int ano;
    DatePicker dataProt;
    String url ="http://159.203.75.66/pat/protocolo";

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_protocolo, container, false);

        cadastrarProtBT = (Button) v.findViewById(R.id.cadastrarProtBT);
        origem = (EditText) v.findViewById(R.id.origemID);
        destino = (EditText) v.findViewById(R.id.destinoID);
        dataProt = (DatePicker) v.findViewById(R.id.dataProtocolo);
        idObjeto = (EditText) v.findViewById(R.id.idObjetoProtocolo);

        cadastrarProtBT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                dia = dataProt.getDayOfMonth();
                mes = dataProt.getMonth() + 1;
                ano = dataProt.getYear();

                data = dia + "/" + mes + "/" + ano;


                RequestQueue queue = Volley.newRequestQueue(getContext());

// POST parameters
                Map<String, String> params = new HashMap<String, String>();
                params.put("origem", origem.getText().toString());
                params.put("destino", destino.getText().toString());
                params.put("idObjeto", idObjeto.getText().toString());
                params.put("data", data);
                params.put("idUsuario", "1");

                JSONObject jsonObj = new JSONObject(params);

// Request a json response from the provided URL
                JsonObjectRequest jsonObjRequest = new JsonObjectRequest
                        (Request.Method.POST, url, jsonObj, new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                Toast.makeText(getContext(), "Cadastrado com Sucesso! " + response.toString(), Toast.LENGTH_SHORT).show();
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
