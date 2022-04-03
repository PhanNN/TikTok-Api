## Get Video's Comments Doc

### Required inputs
```
  headers: {
    "cookie": "",
    "custom_verifyFp": "",
    "custom_device_id": "",
    "ms_token": "",
    "x_bogus": ""
  },
  params: {
    "id": "", // video id
    "cursor": 0,
    "count": 20
  }
```

### Command
```
  python examples/get_comments.py ' _headers_ ' ' _params_ '
```

### Example
```
  python3 examples/get_comments.py '{"cookie": "passport_csrf_token_default=2fda59a4e969e3d1f0ea05549f9b2702; passport_csrf_token=2fda59a4e969e3d1f0ea05549f9b2702; passport_auth_status=4ff043eb76064ecde1cf461509b4f6db%2C; passport_auth_status_ss=4ff043eb76064ecde1cf461509b4f6db%2C; uid_tt=52fb74b0c34da08b486f185d07f95db7df8fca55f955939fedcb5884e0c0a36c; uid_tt_ss=52fb74b0c34da08b486f185d07f95db7df8fca55f955939fedcb5884e0c0a36c; sid_tt=10d0c83a8cb5bc62aeca10d4fa50d0a3; sessionid=10d0c83a8cb5bc62aeca10d4fa50d0a3; sessionid_ss=10d0c83a8cb5bc62aeca10d4fa50d0a3; store-country-code=vn; d_ticket=b04397bdad631b9cd98d098cd616c839c5c17; MONITOR_WEB_ID=131adad0-af2a-49d1-b4f3-d4dbea4bafff; MONITOR_DEVICE_ID=68407210-ed53-4419-8a1e-7a6cceba6112; _tea_utm_cache_3053={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22ios%22%2C%22utm_campaign%22:%22client_share%22}; tt_csrf_token=V2yhVXB_bGdt5NZIf-huYVWf; _tea_utm_cache_1988={%22utm_source%22:%22more%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; sid_guard=10d0c83a8cb5bc62aeca10d4fa50d0a3%7C1637632701%7C5184000%7CSat%2C+22-Jan-2022+01%3A58%3A21+GMT; sid_ucp_v1=; ssid_ucp_v1=; store-idc=useast2a; s_v_web_id=verify_kwbg880r_VtR2KEbz_Tceb_4Jdi_8UcW_70nFesxlS99d; R6kq3TV7=AJofkU99AQAAHC8xsmKwH6yThtdOfYhnNwG5lVc7hI2GMbhi2_AvS5pUC1OX|1|0|97b6e2dec98cd7d5bf82e85a80a9a773af2ce503; cmpl_token=AgQQAPOFF-RMpbEscalR_N0j-vl_TNuev4MOYMPmyQ; ttwid=1%7CLLu0ieofAuUObBpZRUncsMCwzZ24Ah47qKpNxBOibHQ%7C1637717596%7Ca1387a9e331fd64fdc9fe18830c01b11a3a1a8739fdb1d7c973e66645da38fc7; msToken=XK600JC6FWzTwj4pmEFf54Iyg2eXRr9LiEGxT4v5lZQEnBlhBckaLBXPRJvIydAMk7aaNyLlS84K4u4EVjZU0HbrgsBKiJAHm3IOiuAr2wT4cqF3UouOfL1ea4ldiZ7cKt-bTsKzZQ==; __tea_cookie_tokens_1988=%257B%2522web_id%2522%253A%2522%2522%252C%2522timestamp%2522%253A1637717610517%257D; passport_fe_beating_status=true; odin_tt=b56707c3f1f7de4aa0c1f43a94678de798043784296f70a5f9af2637fe030e80ccbc3c400c2b36a3d0a2d4d7c54aaa04893ff3cebeee60eeeea1e38adecbf76f","custom_verifyFp": "verify_kwbg880r_VtR2KEbz_Tceb_4Jdi_8UcW_70nFesxlS99d","custom_device_id": "6960566659182593537","ms_token": "HDHCo7XQjC1zkDRBRuJ-2AWp2yrP-pEVfu9RoSajFFGxF3rwvc-mJ6sGtA7W6q5rRRmdywzGgiX98nku92TH6b9SY3g1Jw-JrUTj9IZ2rzhTwlh7-h3nBuBiU6iKjf0dBBMkaE4=&X-Bogus=DFSzswSOXdkANn/-S7bwqQYklTIX","x_bogus": "DFSzswSOXdkANn/-S7bwqQYklTIX"}' '{"id": "7029962662695980314", "cursor": 0, "count": 20}'
```


### Get user profile by nickname
```
  python3 examples/get_a_user_by_nickname.py phamhuynhnhu1507 '{"cookie": "tt_webid_v2=6969440012124210689; tt_webid=6969440012124210689; tt_csrf_token=1-msMLvHjFmYcDZHXqJilVSY; R6kq3TV7=AFNsuch7AQAAv1p2xRl4GElt0jzjQZvXT6w1BslMU_BUDT09-H9nDkd_6pdl|1|0|424bc099cb6471bc913f62b9213735acc0289660; passport_csrf_token_default=9afb47d69d5d0ddaf0863ecc7ae71749; passport_csrf_token=9afb47d69d5d0ddaf0863ecc7ae71749; sid_guard=ea3c140cb1ddb3965c6e99720bb16553%7C1631160264%7C5184000%7CMon%2C+08-Nov-2021+04%3A04%3A24+GMT; uid_tt=d15016cd37246ce1027252b6ab3d58538a30ea60bcb2426d065d3f3961db4846; uid_tt_ss=d15016cd37246ce1027252b6ab3d58538a30ea60bcb2426d065d3f3961db4846; sid_tt=ea3c140cb1ddb3965c6e99720bb16553; sessionid=ea3c140cb1ddb3965c6e99720bb16553; sessionid_ss=ea3c140cb1ddb3965c6e99720bb16553; sid_ucp_v1=1.0.0-KDYyNzc3OTFhMDFhNmI5YTNlZTJlODM5ZWIwZDI2ZDRhM2I4MGJiNTUKIAiBgLDKg7DE2FoQyI_miQYYswsgDDC4rcTVBTgHQPQHEAEaA3NnMSIgZWEzYzE0MGNiMWRkYjM5NjVjNmU5OTcyMGJiMTY1NTM; ssid_ucp_v1=1.0.0-KDYyNzc3OTFhMDFhNmI5YTNlZTJlODM5ZWIwZDI2ZDRhM2I4MGJiNTUKIAiBgLDKg7DE2FoQyI_miQYYswsgDDC4rcTVBTgHQPQHEAEaA3NnMSIgZWEzYzE0MGNiMWRkYjM5NjVjNmU5OTcyMGJiMTY1NTM; store-idc=alisg; store-country-code=vn; msToken=N2DG9j4A9HYC26K6fNmJ5Dbhe4On6lxnKnAlbiyPHQzsGK1Nr2Hx73HL9Wba4GhenEMPIxgZ772Jcv-pnSH17zZ2vwenlmJldLLF4-iOa8h17B3w-3YP55hvyRAUs3t1v2Os5B4=; cmpl_token=AgQQAPPdF-RMpYqP_yexftk4-tn18EGR_4MOYP1Low; odin_tt=aa1a5084c2c4620114dd007c1c48765ef1ce652848bcebf7a2c91fb7d31be7ee7d517403f6aeb22104d44600909953706fb2e71be08d9cd0f7b8319dd20884bdcc0adf73184e727feb979bf66f3fc1d0; ttwid=1%7C1g_r4wf3HqDyiqi8D-tXFWeuzhsUhCWLXRLeYqY9YIY%7C1631160467%7C9022660fd32d16985f7e70c44df72ba8cbe9dd3487799286c19130743e3c438c","custom_verifyFp": "verify_ktceo1xv_yPqIox5f_UgjY_47pj_ADy9_gWq65DpVGaea","custom_device_id": "6969440012124210689","ms_token": "C96KUn3JgPTN53EDsx9qlQiL-4MRm85M_0C5pq8LvYSjHPdctvmo2_1UrErqBeNSvQF3CLKBOfPyZc5xOqIkcM_m7PzRdiim7a09x_pTzisV_Eh0Z4bQmEUyyRPSaRG4m7UWHon6&X-","x_bogus": "DFSzKwVONHIokqRASYxpLN7Tlqe6"}'

  python3 examples/get_a_user_by_nickname.py phamhuynhnhu1507 '{"cookie": "tt_csrf_token=3j8lu1m_1TKkmiPYFVogzaTG; csrf_session_id=d8ab8ba68dfb49f79c15b295de3aae5f; MONITOR_DEVICE_ID=cb6e3b39-aa46-436d-a797-93e7a7c05ad9; s_v_web_id=verify_kszh87gj_J3kgXukK_RTDV_4Rjj_AnJd_wtBUUnlUaJ0H; csrf_session_id=d8ab8ba68dfb49f79c15b295de3aae5f; _tea_utm_cache_1988={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22ios%22%2C%22utm_campaign%22:%22client_share%22}; passport_csrf_token_default=e1a5d48df5d99f3ef090004eb2a2a664; passport_csrf_token=e1a5d48df5d99f3ef090004eb2a2a664; R6kq3TV7=ADE152l9AQAAkKEkqud4ybWl0MPbWRTPC5yO3K27X_P8plubu9Hs80VVhXaZ|1|0|9fdc48240f7b2b6018f0c189dd5b2209c8a07b7f; d_ticket=02989aa76c6e48043483d59133f2bd3b2fc6c; passport_auth_status=a90c0697a41054a3d4b926dcf8e44bc0%2C; passport_auth_status_ss=a90c0697a41054a3d4b926dcf8e44bc0%2C; sid_guard=4cda02f275dd9ebe763967a721c58092%7C1638159362%7C5184000%7CFri%2C+28-Jan-2022+04%3A16%3A02+GMT; uid_tt=57c485f2e01dad834e7e6948649e5beee43a3ed7547b1734b992ac1979e7f258; uid_tt_ss=57c485f2e01dad834e7e6948649e5beee43a3ed7547b1734b992ac1979e7f258; sid_tt=4cda02f275dd9ebe763967a721c58092; sessionid=4cda02f275dd9ebe763967a721c58092; sessionid_ss=4cda02f275dd9ebe763967a721c58092; sid_ucp_v1=1.0.0-KGM2MDgwYjhkMGI4YzQ0NzMyNzgxNzk3NjNiM2M2MTViNzYzZDc5Y2QKIAiBiKDcjoKYvGEQgqiRjQYYswsgDDDqueOLBjgCQOwHEAEaA3NnMSIgNGNkYTAyZjI3NWRkOWViZTc2Mzk2N2E3MjFjNTgwOTI; ssid_ucp_v1=1.0.0-KGM2MDgwYjhkMGI4YzQ0NzMyNzgxNzk3NjNiM2M2MTViNzYzZDc5Y2QKIAiBiKDcjoKYvGEQgqiRjQYYswsgDDDqueOLBjgCQOwHEAEaA3NnMSIgNGNkYTAyZjI3NWRkOWViZTc2Mzk2N2E3MjFjNTgwOTI; store-idc=useast2a; store-country-code=vn; msToken=8lnvdXa8hAXgeRqJFxAG9fr9Fv22wcWswCkHah1grGUTbwjuRk9H9BMWX4bvx1DJC1-MT2IHJj3cw-sZSmkyXuxVLAvWzRimExfFfG62OMUW72LlZneW_-LsgDMTmJ4Kqkybdl8=; cmpl_token=AgQQAPOFF-RMpbFGjrdjut04-njY12HOv4AOYMMD9A; __tea_cookie_tokens_1988=%257B%2522web_id%2522%253A%2522%2522%252C%2522timestamp%2522%253A1638159383778%257D; passport_fe_beating_status=true; odin_tt=86d6331a6c6a41ee5f02d66213752d51fc9e0b0fb290ce53c8ac1d71d39f8428a0126cd18ebbf9f133023e4811c11dfd5b20f91754fcd7b113928c6ec2a4f806d2b94cb4a2ce104c6ec5b36ceba2dd97; ttwid=1%7CNGz1ovgaLZZ3H3azUEwHW6Zqh_lXInj3gTN988p52A8%7C1638159385%7C4ad1440348ce0886be23400afc92bdbdba19f562b1f6b5cc165b68f91b4e4875; msToken=66BeFgX0WblgeTD1SfBk7YcNqlhGighFAUAUhfw3F6g1ferNPPj-foF-_rw_rmlgeSlwxnEmg4rSIgcnvdFdLLwoZzP6e1xE2iCmvviKTG2_zOnubo9fQecFhC6nS0F88MJdZc4=", "custom_verifyFp": "verify_kszh87gj_J3kgXukK_RTDV_4Rjj_AnJd_wtBUUnlUaJ0H", "custom_device_id": "6924638353028646402", "ms_token": "66BeFgX0WblgeTD1SfBk7YcNqlhGighFAUAUhfw3F6g1ferNPPj-foF-_rw_rmlgeSlwxnEmg4rSIgcnvdFdLLwoZzP6e1xE2iCmvviKTG2_zOnubo9fQecFhC6nS0F88MJdZc4=", "x_bogus": "DFSzswVOqrjcpIH-SidfXN7TlqtQ"}'
```


### Get user tiktoks
```
  python3 examples/get_tiktoks_by_username.py 6769588252283716613 MS4wLjABAAAAPel31WMIBL6basRP3q_EuKmtxfO4nLifBwfKvefN6wnFagii1Xhgos7FnsNoKA6D 12 0
```
