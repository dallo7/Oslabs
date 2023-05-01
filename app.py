# -*- coding: utf-8 -*-
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import dash
import dash_auth
import Dashauth


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], title='OSLabs')
server = app.server
auth = dash_auth.BasicAuth(
    app,
    Dashauth.VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = dbc.Container([
    dbc.Row(
        [
            html.Div([html.P(['OSLabs SMS Service'], id='sms',
                             style={'marginBottom': 15, 'marginTop': 15, 'text-align': 'center', 'color': 'Green',
                                    'fontSize': 20})]),
            html.Br(),
            html.Br(),
            dbc.Col([
                html.Div([
                    dbc.Label("NAME"),
                    dbc.Input(id='name', placeholder="enter name...", type="text"),
                    dbc.FormText("Please enter name"),
                ], style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
                html.Div([
                    dbc.Label("PHONE NUMBER"),
                    dbc.Input(id='phonenumber', placeholder="enter phone number...", type="number"),
                    dbc.FormText("Please type phone number"),
                ], style={'marginBottom': 15, 'marginTop': 5, 'color': 'Green', 'fontSize': 14}),
                html.Div([
                    dbc.Label("ENTER AMOUNT"),
                    dbc.Input(id='amount', placeholder="enter amount...", type="number"),
                    dbc.FormText("Please enter amount of money transacted"),
                ], style={'marginBottom': 20, 'marginTop': 20, 'color': 'Green', 'fontSize': 14}),
            ]),
            html.Br(),
            html.Div(id='response'),
            html.Br(),
            html.Div(
                [
                    dbc.Button(
                        "Submit", id="submit", color="success", n_clicks=0,
                        style={"verticalAlign": "middle"}
                    )
                ],
            )
        ], style={'backgroundColor': 'F0E68C'}
    )
], style={'backgroundColor': 'F0E68C', 'marginTop': '20px', 'marginRight': '20px', 'marginBottom': '40px',
          'marginLeft': '20px', "border": "2px LightGreen"})


@app.callback(Output('response', 'children'),
              Input('submit', 'n_clicks'),
              State('name', 'value'),
              State('phonenumber', 'value'),
              State('amount', 'value'), prevent_initial_call=True)
def update_output(n_clicks, state1, state2, state3):
    if n_clicks > 0 and len(str(state2)) == 9:

        import sms

        text = f'Dear {state1}, your payment of {state3} Kshs to OSLabs has been processed successfully.'

        response = sms.send_sms(int(state2), text)

        if response.status_code == 200:
            return 'Message sent successfully'
        else:
            return 'Invalid entry'
    else:
        return "Please Re-check the Phone number and try again!"


if __name__ == "__main__":
    app.run_server(debug=True)
