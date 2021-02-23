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
      body: CenteredView(
        child: Column(
          children: <Widget>[
            NavigationBar(),
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
