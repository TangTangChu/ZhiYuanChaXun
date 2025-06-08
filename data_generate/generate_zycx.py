import requests
data=[{'text': '北京', 'selected': '0', 'options': [{'text': '2024本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2024专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2023本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2022本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2021本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2020本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '天津', 'selected': '0', 'options': [{'text': '2024本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2024专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2023本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2022本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2021本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2020本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '河北', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '山西', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '内蒙古', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '辽宁', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '吉林', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '黑龙江', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '上海', 'selected': '0', 'options': [{'text': '2024本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2024专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2023本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2022本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2021本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2020本科', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020专科', 'selected': '0', 'options': [{'text': '语数外', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}]}, {'text': '江苏', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '浙江', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}]}, {'text': '安徽', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '福建', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '江西', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023本科', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022本科', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021本科', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020本科', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '山东', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '河南', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '湖北', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '湖南', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '广东', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '广西', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '海南', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '3+3综合', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '重庆', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '四川', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '贵州', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '云南', 'selected': '1', 'options': [{'text': '2024', 'selected': '1', 'options': [{'text': '理科', 'selected': '1'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '西藏(暂无数据)', 'selected': '0', 'options': [], 'disabled': True}, {'text': '陕西', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '甘肃', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '物理类', 'selected': '0'}, {'text': '历史类', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '青海', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '宁夏', 'selected': '0', 'options': [{'text': '2024', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2023', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2022', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2021', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2020', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2019', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}, {'text': '2018', 'selected': '0', 'options': [{'text': '理科', 'selected': '0'}, {'text': '文科', 'selected': '0'}]}]}, {'text': '新疆(暂无数据)', 'selected': '0', 'options': [], 'disabled': True}]
a='''data'''
a=a.split('\n')
arr={}
for i in a:
    b=i.split('\t')
    if not b[0] in arr:
        arr[b[0]]={}
    if not b[1] in arr[b[0]]:
        arr[b[0]][b[1]]={}
    if not b[2] in arr[b[0]][b[1]]:
        if b[4]=='-':
            b[4]=b[5]
        if b[5]=='-':
            b[5]=b[4]
        arr[b[0]][b[1]][b[2]]={'num':b[3],'max':b[4],'min':b[5],'avg':b[6],'maxorder':'-','minorder':'-'}

for i in arr:
    query_1=None
    for j in data:
        if i in j['text']:
            query_1=j
            break
    if query_1 is None:
        prov=input(f'未找到 {i} 的数据，请输入正确的值，或输入 pass 跳过：')
        if prov=='' or 'pass' in prov:
            continue
        else:
            for j in data:
                if prov in j['text']:
                    query_1=j
                    break
            if query_1 is None:
                print(f'未找到 {prov} 的数据，已跳过：')
                continue
    print('当前有如下批次')
    for j in query_1['options']:
        print(j['text'])
    query_2=None
    level=input('请输入批次，如无批次请输入 pass 跳过：')
    if level=='' or 'pass' in level:
        continue
    for j in query_1['options']:
        if level in j['text']:
            query_2=j
    if query_2 is None:
        print(f'未找到 {level} 的数据，已跳过：')
        continue
    for j in arr[i]:
        query_3=None
        for k in query_2['options']:
            if j in k['text']:
                query_3=k
                break
        if query_3 is None:
            print(f'未找到 {j} 的数据，当前有如下数据：')
            for k in query_2['options']:
                print(k['text'])
            types=input('请输入正确的值，或输入 pass 跳过：')
            if types=='' or 'pass' in types:
                continue
            else:
                for k in query_2['options']:
                    if types in k['text']:
                        query_3=k
                        break
                if query_3 is None:
                    print(f'未找到 {types} 的数据，已跳过：')
                    continue
        params={
            'fromCard': 1,
            'resource_id': 50266,
            'province': query_1['text'],
            'year': query_2['text'],
            'category': query_3['text'],
            'query': '一分一段'
        }
        res=requests.get('https://opendata.baidu.com/api.php',params=params,verify=False).json()
        seginfo=res['Result'][0]['DisplayData']['resultData']['tplData']['segmentInfo']
        seglist=[]
        for s in seginfo:
            seg=list(map(int,s['segment'].split('-')))
            seglist.append({'max':seg[0],'min':seg[1],'info':s['segList']})
        for k in arr[i][j]:
            max_score=arr[i][j][k]['max']
            min_score=arr[i][j][k]['min']
            if max_score=='-' or min_score=='-':
                continue
            score=int(max_score)
            for seg in seglist:
                if score>=seg['min'] and score<=seg['max']:
                    info=seg['info']
                    for inf in info:
                        if score>=int(inf['minScore']) and score<=int(inf['maxScore']):
                            arr[i][j][k]['maxorder']=inf['minOrder']
                            break
                    break
            score=int(min_score)
            for seg in seglist:
                if score>=seg['min'] and score<=seg['max']:
                    info=seg['info']
                    for inf in info:
                        if score>=int(inf['minScore']) and score<=int(inf['maxScore']):
                            arr[i][j][k]['minorder']=inf['maxOrder']
                            break
                    break

area_type='$AreaType = array(\n'
for i in arr:
    area_type+=f"    '{i}' => array("
    for j in arr[i]:
        area_type+=f"'{j}', "
    area_type=area_type[:-2]
    area_type+='),\n'
area_type=area_type[:-2]
area_type+='\n);'

def calc_max_min(arr):
    max_order=99999999
    min_order=0
    for i in arr:
        if arr[i]['maxorder']!='-':
            max_order=min(max_order,int(arr[i]['maxorder']))
        if arr[i]['minorder']!='-':
            min_order=max(min_order,int(arr[i]['minorder']))
    if max_order<=min_order:
        return str(max_order),str(min_order)
    else:
        return '0','0'

area_score='$AreaScore = array(\n'
for i in arr:
    area_score+=f"    '{i}' => array("
    for j in arr[i]:
        max_min=calc_max_min(arr[i][j])
        area_score+=f"'{j}' => array({max_min[0]}, {max_min[1]}), "
    area_score=area_score[:-2]
    area_score+='),\n'
area_score=area_score[:-2]
area_score+='\n);'

subject='$Subject = array(\n'
for i in arr:
    subject+=f"    '{i}' => array(\n"
    for j in arr[i]:
        subject+=f"        '{j}' => array(\n"
        for k in arr[i][j]:
            subject+=f"            '{k}' => array('Num' => {arr[i][j][k]['num'] if arr[i][j][k]['num']!='-' else '0'}, 'MaxScore' => {arr[i][j][k]['max'] if arr[i][j][k]['max']!='-' else '0'}, 'MinScore' => {arr[i][j][k]['min'] if arr[i][j][k]['min']!='-' else '0'}, 'AvgScore' => {arr[i][j][k]['avg'] if arr[i][j][k]['avg']!='-' else '0'}, 'MaxRank' => {arr[i][j][k]['maxorder'] if arr[i][j][k]['maxorder']!='-' else '0'}, 'MinRank' => {arr[i][j][k]['minorder'] if arr[i][j][k]['minorder']!='-' else '0'}),\n"
        subject=subject[:-2]
        subject+='\n        ),\n'
    subject=subject[:-2]
    subject+='\n    ),\n'
subject=subject[:-2]
subject+='\n);'

with open('temp_info.php','w',encoding='utf-8') as f:
    f.write('<?php\n')
    f.write(area_type)
    f.write('\n')
    f.write(area_score)
    f.write('\n')
    f.write(subject)
    f.write('\n?>')
