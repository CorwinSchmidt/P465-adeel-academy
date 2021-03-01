import 'package:flutter/material.dart';
import 'package:learning_management_system/widgets/centered_view/centered_view.dart';
import 'package:learning_management_system/widgets/details/details.dart';
import 'package:learning_management_system/widgets/log_in/log_in.dart';
import 'package:learning_management_system/widgets/navigation/nav_drawer.dart';

// This is the home view for our web page.
class StartingDashView extends StatelessWidget {
  const StartingDashView({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Image.asset('assets/images/logo.png'),
        toolbarHeight: 80,
        backgroundColor: Colors.red[700],
      ),
      drawer: NavDrawer(),
      body: CenteredView(
        child: Text("This is our dashboard. I am having so much fun. This is so fun."),
        // child: Column(
        //   children: <Widget>[
        //     //NavigationBar(),
        //     Expanded(
        //       child: Row(
        //         children: <Widget>[
        //           Details(),
        //           Expanded(
        //             child: Center(
        //               child: LogIn('Log In', 'Sign Up'),
        //             ),
        //           ),
        //         ],
        //       ),
        //     ),
        //   ],
        // ),
      ),
    );
  }
}
