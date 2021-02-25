import 'package:flutter/material.dart';
import 'package:learning_management_system/assets.dart';
import 'package:learning_management_system/objects/pages.dart';

final Content heatMapContent = Content(
  name: 'Heat Map',
  imageUrl: Assets.heatmap_demo,
  titleImageUrl: "User Conversions",
  videoUrl: "Enter Video URL Here",
  description:
      'This is a Heat Map to Visually Represent the Journeys of Converted Users on a Given Page',
);

final List<Content> keyMetrics = const [
  Content(
      name: "Weekly Conversions",
      imageUrl: Assets.weekly_conversions,
      color: Colors.blueGrey,
      titleImageUrl: "Weekly Conversions Bar Chart"),
  Content(
      name: "Total Users to Conversions",
      imageUrl: Assets.usersToConversions,
      color: Colors.deepPurple,
      titleImageUrl: "Total Users to Conversions"),
  Content(
      name: "Conversion Growth",
      imageUrl: Assets.demo_key_metrics,
      color: Colors.orange,
      titleImageUrl: "Key Metrics Line Chart"),
  Content(
      name: "Daily Conversions",
      imageUrl: Assets.conversion_rate_example,
      color: Colors.yellow,
      titleImageUrl: "Daily Conversion Line Chart"),
  Content(
      name: "Conversion Growth Rate",
      imageUrl: Assets.conversion_growth,
      color: Colors.purple,
      titleImageUrl: "Conversion Growth Rate"),
  Content(
      name: "Average Time on Site",
      imageUrl: Assets.average_time_on_site,
      color: Colors.green,
      titleImageUrl: "Average Time Spent on the Site"),
  Content(
      name: "Traffic Sources to the Site",
      imageUrl: Assets.traffic_sources,
      color: Colors.red,
      titleImageUrl: "Traffic Sources to the Site"),
  Content(
      name: "Social Media Dashboard",
      imageUrl: Assets.social_media_dashboard,
      color: Colors.lightBlue,
      titleImageUrl: "Social Media Dashboard"),
  Content(
      name: "Cost Aquisition per Customer",
      imageUrl: Assets.cost_acquisition,
      color: Colors.lightGreen,
      titleImageUrl: "Cost Aquisition per Customer"),
  Content(
      name: "KPI Dashboard",
      imageUrl: Assets.kpi_dashboard,
      color: Colors.deepOrange,
      titleImageUrl: "KPI Dashboard"),
];

final List<Content> highlights = const [
  Content(
    name: "Average Time on Site",
    imageUrl: Assets.average_time_on_site,
  ),
  Content(
    name: "Total Users to Conversions",
    imageUrl: Assets.usersToConversions,
  ),
  Content(
    name: "Traffic Sources to the Site",
    imageUrl: Assets.traffic_sources,
  ),
  Content(
    name: "Social Media Dashboard",
    imageUrl: Assets.social_media_dashboard,
  ),
  Content(
    name: "Cost Aquisition per Customer",
    imageUrl: Assets.cost_acquisition,
  ),
  Content(name: "KPI Dashboard", imageUrl: Assets.kpi_dashboard),
  Content(
    name: "Weekly Conversions",
    imageUrl: Assets.weekly_conversions,
  ),
  Content(
    name: "Conversion Growth",
    imageUrl: Assets.demo_key_metrics,
  ),
  Content(
    name: "Daily Conversions",
    imageUrl: Assets.conversion_rate_example,
  ),
  Content(
    name: "Conversion Growth Rate",
    imageUrl: Assets.conversion_growth,
  ),
];

final List<Content> lowlights = const [
  Content(
    name: "Total Users to Conversions",
    imageUrl: Assets.usersToConversions,
  ),
  Content(
    name: "Social Media Dashboard",
    imageUrl: Assets.social_media_dashboard,
  ),
  Content(
    name: "Cost Aquisition per Customer",
    imageUrl: Assets.cost_acquisition,
  ),
  Content(name: "KPI Dashboard", imageUrl: Assets.kpi_dashboard),
  Content(
    name: "Weekly Conversions",
    imageUrl: Assets.weekly_conversions,
  ),
  Content(
    name: "Conversion Growth",
    imageUrl: Assets.demo_key_metrics,
  ),
  Content(
    name: "Daily Conversions",
    imageUrl: Assets.conversion_rate_example,
  ),
  Content(
    name: "Conversion Growth Rate",
    imageUrl: Assets.conversion_growth,
  ),
  Content(
    name: "Average Time on Site",
    imageUrl: Assets.average_time_on_site,
  ),
  Content(
    name: "Traffic Sources to the Site",
    imageUrl: Assets.traffic_sources,
  ),
];

final List<Content> recommended = const [
  Content(
    name: "Cost Aquisition per Customer",
    imageUrl: Assets.cost_acquisition,
  ),
  Content(
    name: "Daily Conversions",
    imageUrl: Assets.conversion_rate_example,
  ),
  Content(
    name: "Conversion Growth Rate",
    imageUrl: Assets.conversion_growth,
  ),
  Content(
    name: "Average Time on Site",
    imageUrl: Assets.average_time_on_site,
  ),
  Content(
    name: "Traffic Sources to the Site",
    imageUrl: Assets.traffic_sources,
  ),
  Content(
    name: "Total Users to Conversions",
    imageUrl: Assets.usersToConversions,
  ),
  Content(
    name: "Weekly Conversions",
    imageUrl: Assets.weekly_conversions,
  ),
  Content(
    name: "Conversion Growth",
    imageUrl: Assets.demo_key_metrics,
  ),
  Content(
    name: "Social Media Dashboard",
    imageUrl: Assets.social_media_dashboard,
  ),
  Content(name: "KPI Dashboard", imageUrl: Assets.kpi_dashboard),
];
