import 'package:flutter/material.dart';
import 'package:learning_management_system/views/dashboard/starting_dash_view.dart';
import 'package:learning_management_system/views/home/home_view.dart';
import 'package:learning_management_system/assets.dart';
import 'package:learning_management_system/widgets/centered_view/centered_view.dart';

// This will be the page that opens whenever user presses the LogIn button
class SignupView extends StatelessWidget {
  // controller for email textfield
  final emailController = TextEditingController();
  // controller for password textfield
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sign Up"),
        backgroundColor: Colors.red[700],
      ),
      body: CenteredView(
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
                      controller:
                          emailController, // add controller to textfield
                    ),
                    TextFormField(
                      decoration: new InputDecoration(
                        labelText: "Password:",
                      ),
                      obscureText: true,
                      keyboardType: TextInputType.text,
                      controller:
                          passwordController, // add controller to textfield
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
                      child: Text("Sign up"),
                      onPressed: () {
                        
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => StartingDashView()),
                        );
                        
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
