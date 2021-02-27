import 'package:flutter/material.dart';
import 'package:learning_management_system/pages/screens.dart';
import 'package:learning_management_system/assets.dart';
import 'package:learning_management_system/pages/nav_screen.dart';
import 'package:learning_management_system/views/home/home_view.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Adeel Academy',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.red,
        visualDensity: VisualDensity.adaptivePlatformDensity,
        scaffoldBackgroundColor: Colors.white,
      ),
      home: HomeView(),
    );
  }
}

class LoginPage extends StatefulWidget {
  @override
  State createState() => new LoginPageState();
}

class LoginPageState extends State<LoginPage>
    with SingleTickerProviderStateMixin {
  Animation<double> _iconAnimation;
  AnimationController _iconAnimationController;

  @override
  void initState() {
    super.initState();
    _iconAnimationController = new AnimationController(
        vsync: this, duration: new Duration(milliseconds: 500));
    _iconAnimation = new CurvedAnimation(
      parent: _iconAnimationController,
      curve: Curves.bounceOut,
    );
    _iconAnimation.addListener(() => this.setState(() {}));
    _iconAnimationController.forward();
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      //backgroundColor: Color.fromRGBO(7, 7, 12, 0.87),
      backgroundColor: Color.fromRGBO(37, 37, 54, 0.65),
      body: new Stack(fit: StackFit.expand, children: <Widget>[
        // // // new Image(
        // // //   image: AssetImage(Assets.nostra_o),
        // //   fit: BoxFit.cover,
        // //   colorBlendMode: BlendMode.darken,
        // //   color: Colors.black87,
        // ),
        new Theme(
          data: new ThemeData(
              brightness: Brightness.light,
              inputDecorationTheme: new InputDecorationTheme(
                // hintStyle: new TextStyle(color: Colors.blue, fontSize: 20.0),
                labelStyle:
                    new TextStyle(color: Colors.tealAccent, fontSize: 20.0),
              )),
          child: SingleChildScrollView(
            child: new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Padding(padding: EdgeInsets.fromLTRB(0.0, 60.0, 0.0, 0.0)),
                new Image(image: new AssetImage(Assets.nostra_o)),
                new Container(
                  //padding: const EdgeInsets.fromLTRB(0.0, 20.0, 0.0, 0.0),
                  child: new Form(
                    autovalidate: true,
                    child: new Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        new TextFormField(
                          decoration: new InputDecoration(
                              labelText: "Email:", fillColor: Colors.white),
                          keyboardType: TextInputType.emailAddress,
                        ),
                        new TextFormField(
                          decoration: new InputDecoration(
                            labelText: "Password:",
                          ),
                          obscureText: true,
                          keyboardType: TextInputType.text,
                        ),
                        new Padding(
                          padding: const EdgeInsets.only(top: 30.0),
                        ),
                        new MaterialButton(
                          height: 40.0,
                          minWidth: 100.0,
                          color: Colors.orange,
                          splashColor: Colors.teal,
                          textColor: Colors.white,
                          child: Text("Login"),
                          onPressed: () {
                            navigateToNavScreen(context);
                          },
                        )
                      ],
                    ),
                  ),
                )
              ],
            ),
          ),
        ),
      ]),
    );
  }

  Future navigateToNavScreen(context) async {
    Navigator.push(
        context, MaterialPageRoute(builder: (context) => NavScreen()));
  }
}
