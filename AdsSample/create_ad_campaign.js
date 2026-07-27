/**
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 * All rights reserved.
 * @flow
 */

"use strict";
const bizSdk = require("facebook-nodejs-business-sdk");
const AdAccount = bizSdk.AdAccount;
const Campaign = bizSdk.Campaign;

let access_token =
  "EAAVUPqCKmJcBR9tY1Xb9JnQZAkW4SoNeJ2okaPgUwkZCI6cqI2eyeeKEh8vZBiYSIBxLYTUusXNRxt90FqoJ17bqmzIAfVDJOqIffu36RuML853oF7710xeMrW8OQxMcFMREOA9mFEFEUhUiTnly6rZBqArl1DEb7ctlLiKgslHWsUIlwA447cCGNyYez9uKo24dS5vC";
let app_id = "1500002841696407";
let ad_account_id = "act_1649311399744928";
let campaign_name = "";

const api = bizSdk.FacebookAdsApi.init(access_token);
const showDebugingInfo = true; // Setting this to true shows more debugging info.
if (showDebugingInfo) {
  api.setDebug(true);
}

const logApiCallResult = (apiCallName, data) => {
  console.log(apiCallName);
  if (showDebugingInfo) {
    console.log("Data:" + JSON.stringify(data));
  }
};

let fields, params;

void (async function () {
  try {
    // Create an ad campaign with objective OUTCOME_TRAFFIC
    fields = [];
    params = {
      name: campaign_name,
      objective: "OUTCOME_TRAFFIC",
      status: "PAUSED",
      special_ad_categories: [],
    };
    let campaign = await new AdAccount(account_id).createCampaign(
      fields,
      params,
    );
    let campaign_id = campaign.id;

    console.log("Your created campaign is with campaign_id:" + campaign_id);
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
})();
