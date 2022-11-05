DEFAULT_CAL = """
{
  "VCALENDAR": {
    "METHOD": "PUBLISH",
    "VERSION": "2.0",
    "X-WR-CALNAME": "未命名",
    "PRODID": "-//Apple Inc.//macOS 11.6.8//EN",
    "X-APPLE-CALENDAR-COLOR": "#0E61B9",
    "X-WR-TIMEZONE": "Asia/Shanghai",
    "CALSCALE": "GREGORIAN",
    "VTIMEZONE": {
      "TZID": "Asia/Shanghai",
      "STANDARD": {
        "TZOFFSETFROM": "+0900",
        "RRULE": "FREQ=YEARLY;UNTIL=19910914T170000Z;BYMONTH=9;BYDAY=3SU",
        "DTSTART": "19890917T020000",
        "TZNAME": "GMT+8",
        "TZOFFSETTO": "+0800"
      },
      "DAYLIGHT": {
        "TZOFFSETFROM": "+0800",
        "DTSTART": "19910414T020000",
        "TZNAME": "GMT+8",
        "TZOFFSETTO": "+0900",
        "RDATE": "19910414T020000"
      }
    }
  }
}
"""

DEFAULT_EVENT = """
{
    "VEVENT": {
        "CREATED": "20220913T113852Z",
        "UID": "FA596B6B-372B-4BF7-B7B6-9714F4F3FC3D",
        "DTEND;TZID=Asia/Shanghai": "20220914T163000",
        "TRANSP": "OPAQUE",
        "X-APPLE-TRAVEL-ADVISORY-BEHAVIOR": "AUTOMATIC",
        "SUMMARY": "Test",
        "LAST-MODIFIED": "20220913T114106Z",
        "DTSTAMP": "20220913T113901Z",
        "DTSTART;TZID=Asia/Shanghai": "20220914T083000",
        "LOCATION": "",
        "SEQUENCE": 1
    }
}
"""