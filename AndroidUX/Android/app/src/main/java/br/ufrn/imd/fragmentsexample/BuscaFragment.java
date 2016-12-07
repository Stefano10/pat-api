package br.ufrn.imd.fragmentsexample;

import android.app.Activity;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.content.Intent;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.zxing.integration.android.IntentIntegrator;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.FragmentTransaction;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;


public class BuscaFragment extends Fragment {

    private Button buscarBtn;
    private ImageButton scan_btn;
    private EditText tombo;
    TextView descricaoV;
    ProgressBar barra;

    String URLBusca = "http://159.203.75.66/pat/objeto/tombo/";



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment

        View v = inflater.inflate(R.layout.busca_fragment, container, false);

        buscarBtn = (Button) v.findViewById(R.id.buscarbt);

        scan_btn = (ImageButton) v.findViewById(R.id.cameraBuscar);
        tombo = (EditText) v.findViewById(R.id.tomboSerial);
        descricaoV = (TextView) v.findViewById(R.id.descricaoV);
        barra = (ProgressBar) v.findViewById(R.id.progressBar);




        scan_btn.setOnClickListener(new View.OnClickListener(){
           @Override
            public void onClick(View view) {

               IntentIntegrator integrator = new IntentIntegrator(getActivity());

               integrator.setDesiredBarcodeFormats(IntentIntegrator.ALL_CODE_TYPES);

                integrator.setPrompt("Scan");
                integrator.setCameraId(0);
                integrator.setBeepEnabled(false);
                integrator.setBarcodeImageEnabled(false);
                integrator.initiateScan();

         }
         });


        buscarBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            //    FragmentTransaction ft = getActivity().getSupportFragmentManager().beginTransaction();
             //   ft.replace(R.id.content_main, new ResultadoBusca());
              //  ft.addToBackStack(null);
              //  ft.commit();


                if(tombo.getText().toString() !="") {

                    barra.setVisibility(ProgressBar.VISIBLE);
                    RequestQueue queue = Volley.newRequestQueue(getContext());


                    StringRequest stringRequest = new StringRequest(Request.Method.GET, URLBusca+tombo.getText().toString(),
                            new Response.Listener<String>() {
                                @Override
                                public void onResponse(String response) {
                                    // Display the first 500 characters of the response string.
                                    barra.setVisibility(ProgressBar.GONE);
                                    descricaoV.setText(response);
                                }
                            }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            descricaoV.setText("That didn't work!");
                        }
                    });
// Add the request to the RequestQueue.
                    queue.add(stringRequest);


                }

                // Request a string response from the provided URL.


            }

        });



        return v;
    }




}
