import json

emptyData = {"secondaryInfo": ""}
dataWithoutViz = {"secondaryInfo": {"presModelMap": {}}}
dataWithoutPres1 = {"secondaryInfo": {"presModelMap": {"vizData": {}}}}
dataWithoutMapPresModel = {
    "secondaryInfo": {"presModelMap": {"vizData": {"presModelHolder": {}}}}
}
dataWithoutMapPres2 = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {"presModelHolder": {"genPresModelMapPresModel": {}}}
        }
    }
}

noWorksheet = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {"genPresModelMapPresModel": {"presModelMap": {}}}
            }
        }
    }
}

data = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {
                    "genPresModelMapPresModel": {
                        "presModelMap": {
                            "[WORKSHEET1]": {
                                "presModelHolder": {
                                    "genVizDataPresModel": {
                                        "paneColumnsData": {
                                            "paneColumnsList": [
                                                {
                                                    "vizPaneColumns": [
                                                        {
                                                            "valueIndices": [
                                                                1,
                                                                2,
                                                                3,
                                                                4,
                                                            ],
                                                            "aliasIndices": [],
                                                        },
                                                        {
                                                            "valueIndices": [],
                                                            "aliasIndices": [
                                                                -6,
                                                                -7,
                                                                -8,
                                                                -9,
                                                            ],
                                                        },
                                                    ]
                                                }
                                            ],
                                            "vizDataColumns": [
                                                {
                                                    "fieldCaption": "[FIELD1]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [0],
                                                    "isAutoSelect": True,
                                                },
                                                {
                                                    "fieldCaption": "[FIELD2]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [1],
                                                },
                                            ],
                                        }
                                    }
                                }
                            },
                            "[WORKSHEET2]": {
                                "presModelHolder": {"genVizDataPresModel": {}}
                            },
                        }
                    }
                }
            },
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["1", "2", "3", "4", "5", "6"],
                                    },
                                    {"dataType": "real", "dataValues": [1, 2, 3, 4, 5]},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {
                                        "dataType": "cstring",
                                        "dataValues": ["7", "8", "9"],
                                    }
                                ]
                            },
                        }
                    }
                }
            },
        }
    }
}

emptyValues = {
    "secondaryInfo": {
        "presModelMap": {
            "vizData": {
                "presModelHolder": {
                    "genPresModelMapPresModel": {
                        "presModelMap": {
                            "[WORKSHEET1]": {
                                "presModelHolder": {
                                    "genVizDataPresModel": {
                                        "paneColumnsData": {
                                            "paneColumnsList": [
                                                {
                                                    "vizPaneColumns": [
                                                        {
                                                            "valueIndices": [],
                                                            "aliasIndices": [],
                                                        },
                                                        {
                                                            "valueIndices": [],
                                                            "aliasIndices": [],
                                                        },
                                                    ]
                                                }
                                            ],
                                            "vizDataColumns": [
                                                {
                                                    "fieldCaption": "[FIELD1]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [0],
                                                    "isAutoSelect": True,
                                                },
                                                {
                                                    "fieldCaption": "[FIELD2]",
                                                    "dataType": "cstring",
                                                    "paneIndices": [0],
                                                    "columnIndices": [1],
                                                },
                                            ],
                                        }
                                    }
                                }
                            },
                            "[WORKSHEET2]": {
                                "presModelHolder": {"genVizDataPresModel": {}}
                            },
                        }
                    }
                }
            },
            "dataDictionary": {
                "presModelHolder": {
                    "genDataDictionaryPresModel": {
                        "dataSegments": {
                            "0": {
                                "dataColumns": [
                                    {"dataType": "cstring", "dataValues": []},
                                    {"dataType": "real", "dataValues": []},
                                ]
                            },
                            "1": {
                                "dataColumns": [
                                    {"dataType": "cstring", "dataValues": []}
                                ]
                            },
                        }
                    }
                }
            },
        }
    }
}

vqlCmdResponseEmptyValues = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {"visual": {"vizData": {}}},
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {"visual": {"vizData": {}}},
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real", "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring", "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

vqlCmdResponse = {
    "vqlCmdResponse": {
        "layoutStatus": {
            "applicationPresModel": {
                "workbookPresModel": {
                    "dashboardPresModel": {
                        "zones": {
                            "0": {
                                "worksheet": "[WORKSHEET1]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {
                                            "paneColumnsData": {
                                                "paneColumnsList": [
                                                    {
                                                        "vizPaneColumns": [
                                                            {
                                                                "valueIndices": [
                                                                    1,
                                                                    2,
                                                                    3,
                                                                    4,
                                                                ],
                                                                "aliasIndices": [],
                                                            },
                                                            {
                                                                "valueIndices": [],
                                                                "aliasIndices": [
                                                                    -6,
                                                                    -7,
                                                                    -8,
                                                                    -9,
                                                                ],
                                                            },
                                                        ]
                                                    }
                                                ],
                                                "vizDataColumns": [
                                                    {
                                                        "fieldCaption": "[FIELD1]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [0],
                                                    },
                                                    {
                                                        "fieldCaption": "[FIELD2]",
                                                        "dataType": "cstring",
                                                        "paneIndices": [0],
                                                        "columnIndices": [1],
                                                    },
                                                ],
                                            }
                                        }
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME1]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select1",
                                            "select2",
                                            "select3",
                                        ],
                                    },
                                },
                            },
                            "1": {
                                "worksheet": "[WORKSHEET2]",
                                "presModelHolder": {
                                    "visual": {
                                        "vizData": {},
                                    },
                                    "parameterControl": {
                                        "fieldCaption": "[INPUT_NAME2]",
                                        "parameterName": "[Parameters].[Parameter 1]",
                                        "formattedValues": [
                                            "select4",
                                            "select5",
                                            "select6",
                                        ],
                                    },
                                },
                            },
                        }
                    }
                },
                "dataDictionary": {
                    "dataSegments": {
                        "0": {
                            "dataColumns": [
                                {
                                    "dataType": "cstring",
                                    "dataValues": ["1", "2", "3", "4", "5", "6"],
                                },
                                {"dataType": "real", "dataValues": [1, 2, 3, 4, 5]},
                            ]
                        },
                        "1": {
                            "dataColumns": [
                                {"dataType": "cstring", "dataValues": ["7", "8", "9"]}
                            ]
                        },
                    }
                },
            }
        }
    }
}

info = {
    "sheetName": "[SHEET_NAME]",
    "worldUpdate": {
        "applicationPresModel": {
            "workbookPresModel": {
                "dashboardPresModel": {
                    "zones": {
                        "0": {
                            "presModelHolder": {
                                "parameterControl": {
                                    "fieldCaption": "[INPUT_NAME1]",
                                    "parameterName": "[Parameters].[Parameter 1]",
                                    "formattedValues": [
                                        "select1",
                                        "select2",
                                        "select3",
                                    ],
                                }
                            }
                        },
                        "1": {
                            "presModelHolder": {
                                "parameterControl": {
                                    "fieldCaption": "[INPUT_NAME2]",
                                    "parameterName": "[Parameters].[Parameter 1]",
                                    "formattedValues": [
                                        "select4",
                                        "select5",
                                        "select6",
                                    ],
                                }
                            }
                        },
                    }
                }
            }
        }
    },
}

tableauVizHtmlResponse = """
<div>
<textarea id="tsConfigContainer">
{
	"vizql_root": "test",
	"sessionid": "123456:123456",
	"sheetId": "SHEET/NAME"
}
</textarea>
</div>
"""

tableauDataResponse = """
433337;%s433337;%s
""" % (
    json.dumps(info),
    json.dumps(data),
)

fakeUri = "https://public.tableau.com/example"
