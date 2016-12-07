package br.ufrn.imd.fragmentsexample;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.w3c.dom.Text;


public class ResultadoBusca extends Fragment {

    TextView dados;
    String URLBusca = "http://159.203.75.66/pat/objeto/tombo/2012000001";
   // EditText tomboBusca;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View v = inflater.inflate(R.layout.resultado_fragment, container, false);

        dados = (TextView) v.findViewById(R.id.resultadoObjeto);

        //tomboBusca = (EditText)getView().findViewById(R.id.tomboSerial);





// Request a string response from the provided URL.



        return v;
    }


}
