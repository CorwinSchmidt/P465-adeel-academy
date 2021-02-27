import 'package:flutter/material.dart';
import 'package:learning_management_system/widgets/centered_view/centered_view.dart';
import 'package:learning_management_system/widgets/details/details.dart';
import 'package:learning_management_system/widgets/log_in/log_in.dart';
import 'package:learning_management_system/widgets/navigation_bar/navigation_bar.dart';

// This is the home view for our web page.
class HomeView extends StatelessWidget {
  const HomeView({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Image.asset('assets/images/logo.png'),
        toolbarHeight: 80,
        backgroundColor: Colors.red[700],
        ),
        drawer: Drawer(
  elevation: 16.0,
  child: Column(
    children: <Widget>[
      UserAccountsDrawerHeader(
        accountName: Text("xyz"),
        accountEmail: Text("xyz@gmail.com"),
        currentAccountPicture: CircleAvatar(
          backgroundColor: Colors.white,
          child: Text("xyz"),
        ),
        
      ),
      ListTile(
        title: new Text("Courses"),
        leading: new Icon(Icons.mail),
      ),
      Divider(
        height: 0.1,
      ),
      ListTile(
        title: new Text("Primary"),
        leading: new Icon(Icons.inbox),
      ),
      ListTile(
        title: new Text("Social"),
        leading: new Icon(Icons.people),
      ),
      ListTile(
        title: new Text("Promotions"),
        leading: new Icon(Icons.local_offer),
      )
    ],
  ),
),
      body: CenteredView(
        child: Column(
          children: <Widget>[
            //NavigationBar(),
            Expanded(
              child: Row(
                children: <Widget>[
                  Details(),
                  Expanded(
                    child: Center(
                      child: LogIn('Log In', 'Sign Up'),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
