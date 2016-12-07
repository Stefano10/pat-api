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
import android.widget.TextView;
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


public class CautelaFragment extends Fragment {

    Button cautelaBT;
    EditText idObjetoCautela;
    EditText idCautelado;
    DatePicker dataInicio;
    DatePicker dataFim;
    String dataIni;
    String dataF;
    int dia;
    int mes;
    int ano;
    String url ="http://159.203.75.66/pat/cautela";



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_cautela, container, false);


        cautelaBT = (Button) v.findViewById(R.id.cautelaBT);
        idObjetoCautela = (EditText) v.findViewById(R.id.idObjetoCautela);
        idCautelado = (EditText) v.findViewById(R.id.idCautelado);
        dataInicio = (DatePicker) v.findViewById(R.id.dataInicio);
        dataFim = (DatePicker) v.findViewById(R.id.dataFinal);








        cautelaBT.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                dia = dataInicio.getDayOfMonth();
                mes = dataInicio.getMonth()+1;
                ano = dataInicio.getYear();

                dataIni = dia +"/"+mes+"/"+ano;

                dia = dataFim.getDayOfMonth();
                mes = dataFim.getMonth()+1;
                ano = dataFim.getYear();

                dataF = dia +"/"+mes+"/"+ano;

                RequestQueue queue = Volley.newRequestQueue(getContext());

// POST parameters
                Map<String, String> params = new HashMap<String, String>();
                params.put("idUsuario","1");
                params.put("data_inicio", dataIni);
                params.put("data_final", dataF);
                params.put("cautelado",idCautelado.getText().toString());
                params.put("idObjeto",idObjetoCautela.getText().toString());

                JSONObject jsonObj = new JSONObject(params);

// Request a json response from the provided URL
                JsonObjectRequest jsonObjRequest = new JsonObjectRequest
                        (Request.Method.POST, url, jsonObj, new Response.Listener<JSONObject>()
                        {
                            @Override
                            public void onResponse(JSONObject response)
                            {
                                Toast.makeText(getContext(), "Cadastrado com Sucesso! "+response.toString(), Toast.LENGTH_SHORT).show();
                            }
                        },
                                new Response.ErrorListener()
                                {
                                    @Override
                                    public void onErrorResponse(VolleyError error)
                                    {
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
