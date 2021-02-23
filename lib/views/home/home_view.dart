import 'package:flutter/material.dart';
import 'package:learning_management_system/widgets/centered_view/centered_view.dart';
import 'package:learning_management_system/widgets/navigation_bar/navigation_bar.dart';

class HomeView extends StatelessWidget {
  const HomeView({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Column(
        children: <Widget>[
          NavigationBar(),
          CenteredView(
              // Contents of page
              ),
        ],
      ),
      // body: CenteredView(
      //     child: Column(
      //   children: <Widget>[NavigationBar()],
      // ))
    );
  }
}
