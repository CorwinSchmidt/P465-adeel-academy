import 'package:flutter/material.dart';

class LogIn extends StatelessWidget {
  final String text1;
  final String text2;
  LogIn(this.text1, this.text2);

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        //Log In
        Container(
          padding: const EdgeInsets.symmetric(
            horizontal: 60,
            vertical: 15,
          ),
          child: Text(
            text1,
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w800,
              color: Colors.white,
            ),
          ),
          decoration: BoxDecoration(
            color: Colors.red[900],
            borderRadius: BorderRadius.circular(5),
          ),
        ),
        // Spacing:
        SizedBox(height: 10),
        // Sign up:
        Container(
          padding: const EdgeInsets.symmetric(
            horizontal: 60,
            vertical: 15,
          ),
          child: Text(
            text2,
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.w800,
              color: Colors.black,
            ),
          ),
        ),
      ],
    );
  }
}
