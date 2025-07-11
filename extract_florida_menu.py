#!/usr/bin/env python3
"""
Extract Florida Regional Operating Summary menu structure from Experience Builder data
"""

import json

def main():
    """Main function to extract and save Florida menu structure"""
    
    print("🏴 Extracting Florida Regional Operating Summary menu structure...")
    
    # Florida menu structure based on the Experience Builder data
    florida_config = {
        "experienceTitle": "Florida Regional Operating Summary (FLROS)",
        "description": "Covering North Florida, Central Florida & Virgin Islands, and South Florida",
        "baseUrl": "https://experience.arcgis.com/experience/f0cdcfa1d08d48da97197c51c6e3169d",
        "pages": [
            {
                "id": "situational_awareness",
                "title": "1 Situational Awareness",
                "type": "category",
                "color": "purple",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "operating_picture",
                        "title": "Operating Picture",
                        "url": "/page/operating_picture",
                        "views": ["view_195", "view_210"],
                        "searchTerms": ["Operating Picture", "Op Picture"]
                    },
                    {
                        "id": "secar_sitaware",
                        "title": "SECAR SitAware",
                        "url": "/page/secar_sitaware",
                        "views": ["view_224"],
                        "searchTerms": ["SECAR", "Situational Awareness"]
                    }
                ]
            },
            {
                "id": "weather_hazards",
                "title": "2 Weather & Hazards",
                "type": "category",
                "color": "blue",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "weather_maps",
                        "title": "Weather / Maps / Radar",
                        "url": "/page/weather_maps",
                        "views": ["view_208", "view_219"],
                        "searchTerms": ["Weather", "Maps", "Radar"]
                    },
                    {
                        "id": "national_weather",
                        "title": "National Weather",
                        "url": "/page/national_weather",
                        "views": ["view_113", "view_118"],
                        "searchTerms": ["National Weather"]
                    },
                    {
                        "id": "hurricane_center",
                        "title": "National Hurricane Center",
                        "url": "/page/hurricane_center",
                        "views": ["view_114", "view_119", "view_204", "view_222"],
                        "searchTerms": ["Hurricane Center", "NHC"]
                    },
                    {
                        "id": "tropical_atlantic",
                        "title": "Tropical Atlantic",
                        "url": "/page/tropical_atlantic",
                        "views": ["view_203", "view_221"],
                        "searchTerms": ["Tropical Atlantic"]
                    },
                    {
                        "id": "storm_prediction",
                        "title": "Storm Prediction",
                        "url": "/page/storm_prediction",
                        "views": ["view_121", "view_144"],
                        "searchTerms": ["Storm Prediction"]
                    },
                    {
                        "id": "flood_gauges",
                        "title": "Flood Gauges",
                        "url": "/page/flood_gauges",
                        "views": ["view_115", "view_209", "view_220"],
                        "searchTerms": ["Flood Gauges", "River Gauges"]
                    },
                    {
                        "id": "fema_flood",
                        "title": "FEMA Flood",
                        "url": "/page/fema_flood",
                        "views": ["view_205", "view_223"],
                        "searchTerms": ["FEMA Flood"]
                    },
                    {
                        "id": "precipitation",
                        "title": "Precipitation",
                        "url": "/page/precipitation",
                        "views": ["view_120"],
                        "searchTerms": ["Precipitation"]
                    }
                ]
            },
            {
                "id": "logistics_resources",
                "title": "3 Logistics & Resources",
                "type": "category",
                "color": "green",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "trailer_warehouse",
                        "title": "Trailer & Warehouse",
                        "url": "/page/trailer_warehouse",
                        "views": ["view_175", "view_99", "view_100", "view_101", "view_155"],
                        "searchTerms": ["Trailer", "Warehouse", "ERV", "Feeding"]
                    },
                    {
                        "id": "workforce",
                        "title": "Workforce",
                        "url": "/page/workforce",
                        "views": ["view_102", "view_103"],
                        "searchTerms": ["Workforce", "Door"]
                    },
                    {
                        "id": "partnerships",
                        "title": "Partnerships",
                        "url": "/page/partnerships",
                        "views": ["view_104", "view_105", "view_106"],
                        "searchTerms": ["Partnerships", "Latino Engagement", "CARTA"]
                    }
                ]
            },
            {
                "id": "operations",
                "title": "4 Operations",
                "type": "category",
                "color": "orange",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "current_ops",
                        "title": "Current Operations",
                        "url": "/page/current_ops",
                        "views": ["view_129"],
                        "searchTerms": ["Current Operations"]
                    },
                    {
                        "id": "shelter_intake",
                        "title": "Shelter Intake",
                        "url": "/page/shelter_intake",
                        "views": ["view_127"],
                        "searchTerms": ["Shelter Intake"]
                    },
                    {
                        "id": "call_center",
                        "title": "Call Center",
                        "url": "/page/call_center",
                        "views": ["view_128"],
                        "searchTerms": ["Call Center"]
                    },
                    {
                        "id": "disaster_service_tech",
                        "title": "Disaster Service Tech",
                        "url": "/page/disaster_service_tech",
                        "views": ["view_126"],
                        "searchTerms": ["Disaster Service Tech", "DST"]
                    }
                ]
            },
            {
                "id": "response_services",
                "title": "5 Response Services",
                "type": "category",
                "color": "red",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "level_1_2_response",
                        "title": "Level 1-2 Response",
                        "url": "/page/level_1_2_response",
                        "views": ["view_168", "view_107", "view_108", "view_110", "view_111", "view_225"],
                        "searchTerms": ["Level 1-2 Response", "Demographics"]
                    },
                    {
                        "id": "dat_response",
                        "title": "DAT Response",
                        "url": "/page/dat_response",
                        "views": ["view_107", "view_108"],
                        "searchTerms": ["DAT Response"]
                    },
                    {
                        "id": "home_fire_campaign",
                        "title": "Home Fire Campaign",
                        "url": "/page/home_fire_campaign",
                        "views": ["view_110", "view_111", "view_179"],
                        "searchTerms": ["Home Fire Campaign", "HFC"]
                    },
                    {
                        "id": "fd_engage",
                        "title": "FD Engage Dashboard",
                        "url": "/page/fd_engage",
                        "views": ["view_225"],
                        "searchTerms": ["FD Engage"]
                    }
                ]
            },
            {
                "id": "community_data",
                "title": "6 Community Data",
                "type": "category",
                "color": "teal",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "demographics",
                        "title": "Demographics",
                        "url": "/page/demographics",
                        "views": ["view_123"],
                        "searchTerms": ["Demographics"]
                    },
                    {
                        "id": "military_veterans",
                        "title": "Military and Veterans",
                        "url": "/page/military_veterans",
                        "views": ["view_176"],
                        "searchTerms": ["Military", "Veterans"]
                    },
                    {
                        "id": "fema_rapt",
                        "title": "FEMA RAPT",
                        "url": "/page/fema_rapt",
                        "views": ["view_124"],
                        "searchTerms": ["FEMA RAPT"]
                    },
                    {
                        "id": "social_vulnerability",
                        "title": "Social Vulnerability",
                        "url": "/page/social_vulnerability",
                        "views": ["view_145"],
                        "searchTerms": ["Social Vulnerability", "SVI"]
                    }
                ]
            },
            {
                "id": "readiness_metrics",
                "title": "7 Readiness & Metrics",
                "type": "category",
                "color": "indigo",
                "hideFromMenu": False,
                "subPages": [
                    {
                        "id": "national_readiness",
                        "title": "National Readiness",
                        "url": "/page/national_readiness",
                        "views": ["view_136"],
                        "searchTerms": ["National Readiness"]
                    },
                    {
                        "id": "fy_metrics",
                        "title": "FY Metric Report",
                        "url": "/page/fy_metrics",
                        "views": ["view_137"],
                        "searchTerms": ["FY Metrics"]
                    },
                    {
                        "id": "key_program_metrics",
                        "title": "Key Program Metrics",
                        "url": "/page/key_program_metrics",
                        "views": ["view_138"],
                        "searchTerms": ["Key Program Metrics"]
                    },
                    {
                        "id": "hurricane_planning",
                        "title": "Hurricane Planning",
                        "url": "/page/hurricane_planning",
                        "views": ["view_139"],
                        "searchTerms": ["Hurricane Planning"]
                    },
                    {
                        "id": "florida_response",
                        "title": "Florida Response",
                        "url": "/page/florida_response",
                        "views": ["view_140"],
                        "searchTerms": ["Florida Response"]
                    }
                ]
            }
        ],
        "menuConfiguration": {
            "type": "horizontal",
            "style": "pills",
            "spacing": 10,
            "alignment": "center",
            "showIcon": True,
            "submenuExpandMode": "foldable"
        },
        "buttonConfiguration": {
            "featuredButtons": [
                {
                    "title": "Situational Awareness",
                    "targetSection": "situational_awareness",
                    "style": "primary",
                    "icon": "dashboard",
                    "color": "purple"
                },
                {
                    "title": "Weather & Hazards",
                    "targetSection": "weather_hazards",
                    "style": "secondary",
                    "icon": "weather",
                    "color": "blue"
                },
                {
                    "title": "Operations",
                    "targetSection": "operations",
                    "style": "secondary",
                    "icon": "operations",
                    "color": "orange"
                }
            ]
        }
    }
    
    # Save the configuration
    with open('florida_menu_config.json', 'w') as f:
        json.dump(florida_config, f, indent=2)
    
    print(f"✅ Florida menu configuration saved to florida_menu_config.json")
    print(f"📊 Found {len(florida_config['pages'])} main sections")
    
    total_pages = sum(len(page['subPages']) for page in florida_config['pages'])
    print(f"📄 Total sub-pages: {total_pages}")
    
    # Display section summary
    print("\n🗂️  Section Summary:")
    for page in florida_config['pages']:
        print(f"  • {page['title']}: {len(page['subPages'])} pages")

if __name__ == "__main__":
    main() 