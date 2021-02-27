import 'package:flutter/material.dart';
import 'package:learning_management_system/views/home/home_view.dart';
import 'package:learning_management_system/assets.dart';

// This will be the page that opens whenever user presses the LogIn button
class LoginView extends StatelessWidget {

  // controller for email textfield
  final emailController = TextEditingController();
  // controller for password textfield
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Log In"),
        backgroundColor: Colors.red[700],
      ),
      body: Center(
        child: new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Padding(padding: EdgeInsets.fromLTRB(0.0, 60.0, 0.0, 0.0)),
                Image.asset('assets/images/logo.png'),
                new Container(
                  //padding: const EdgeInsets.fromLTRB(0.0, 20.0, 0.0, 0.0),
                  child: new Form(
                    autovalidate: true,
                    child: new Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        TextFormField(
                          decoration: new InputDecoration(
                              labelText: "Email:", fillColor: Colors.white),
                          keyboardType: TextInputType.emailAddress,
                          controller: emailController, // add controller to textfield
                        ),
                        TextFormField(
                          decoration: new InputDecoration(
                            labelText: "Password:",
                          ),
                          obscureText: true,
                          keyboardType: TextInputType.text,
                          controller: passwordController, // add controller to textfield
                        ),
                        Padding(
                          padding: const EdgeInsets.only(top: 30.0),
                        ),
                        MaterialButton(
                          height: 40.0,
                          minWidth: 100.0,
                          color: Colors.orange,
                          splashColor: Colors.teal,
                          textColor: Colors.white,
                          child: Text("Login"),
                          onPressed: () {
                            // temporary onPressed method...
                            // just shows what was entered
                            return showDialog(
                              context: context,
                              builder: (context) {
                                return AlertDialog(
                                  // can use our controllers to get text entered in our two fields
                                  content: Text("Email entered: " + emailController.text + 
                                  "\nPassword entered: " + passwordController.text),
                                );
                              },
                            );
                            // Navigator.push(
                            //   context,
                            //   MaterialPageRoute(builder: (context) => HomeView()),
                            // );
                          },
                        )
                      ],
                    ),
                  ),
                )
              ],
            ),
      ),
    );
  }
}