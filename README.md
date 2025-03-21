# cbbd
This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.20.0
- Package version: 1.20.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```sh
pip install cbbd@1.20.0
```
(you may need to run `pip` with root permission: `sudo pip install cbbd@1.20.0`)

Then import the package:
```python
import cbbd
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cbbd
from cbbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegebasketballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cbbd.Configuration(
    host = "https://api.collegebasketballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cbbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with cbbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cbbd.ConferencesApi(api_client)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)

    try:
        api_response = api_instance.get_conference_history(conference=conference)
        print("The response of ConferencesApi->get_conference_history:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConferencesApi->get_conference_history: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.collegebasketballdata.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConferencesApi* | [**get_conference_history**](docs/ConferencesApi.md#get_conference_history) | **GET** /conferences/history | 
*ConferencesApi* | [**get_conferences**](docs/ConferencesApi.md#get_conferences) | **GET** /conferences | 
*DraftApi* | [**get_draft_picks**](docs/DraftApi.md#get_draft_picks) | **GET** /draft/picks | 
*DraftApi* | [**get_draft_positions**](docs/DraftApi.md#get_draft_positions) | **GET** /draft/positions | 
*DraftApi* | [**get_draft_teams**](docs/DraftApi.md#get_draft_teams) | **GET** /draft/teams | 
*GamesApi* | [**get_broadcasts**](docs/GamesApi.md#get_broadcasts) | **GET** /games/media | 
*GamesApi* | [**get_game_players**](docs/GamesApi.md#get_game_players) | **GET** /games/players | 
*GamesApi* | [**get_game_teams**](docs/GamesApi.md#get_game_teams) | **GET** /games/teams | 
*GamesApi* | [**get_games**](docs/GamesApi.md#get_games) | **GET** /games | 
*LinesApi* | [**get_lines**](docs/LinesApi.md#get_lines) | **GET** /lines | 
*LinesApi* | [**get_providers**](docs/LinesApi.md#get_providers) | **GET** /lines/providers | 
*LineupsApi* | [**get_lineup_stats_by_game**](docs/LineupsApi.md#get_lineup_stats_by_game) | **GET** /lineups/game/{gameId} | 
*LineupsApi* | [**get_lineups_by_team_season**](docs/LineupsApi.md#get_lineups_by_team_season) | **GET** /lineups/team | 
*PlaysApi* | [**get_play_types**](docs/PlaysApi.md#get_play_types) | **GET** /plays/types | 
*PlaysApi* | [**get_plays**](docs/PlaysApi.md#get_plays) | **GET** /plays/game/{gameId} | 
*PlaysApi* | [**get_plays_by_date**](docs/PlaysApi.md#get_plays_by_date) | **GET** /plays/date | 
*PlaysApi* | [**get_plays_by_player_id**](docs/PlaysApi.md#get_plays_by_player_id) | **GET** /plays/player/{playerId} | 
*PlaysApi* | [**get_plays_by_team**](docs/PlaysApi.md#get_plays_by_team) | **GET** /plays/team | 
*PlaysApi* | [**get_plays_by_tournament**](docs/PlaysApi.md#get_plays_by_tournament) | **GET** /plays/tournament | 
*PlaysApi* | [**get_substitutions_by_game**](docs/PlaysApi.md#get_substitutions_by_game) | **GET** /substitutions/game/{gameId} | 
*PlaysApi* | [**get_substitutions_by_player_id**](docs/PlaysApi.md#get_substitutions_by_player_id) | **GET** /substitutions/player/{playerId} | 
*PlaysApi* | [**get_substitutions_by_team**](docs/PlaysApi.md#get_substitutions_by_team) | **GET** /substitutions/team | 
*RankingsApi* | [**get_rankings**](docs/RankingsApi.md#get_rankings) | **GET** /rankings | 
*RatingsApi* | [**get_adjusted_efficiency**](docs/RatingsApi.md#get_adjusted_efficiency) | **GET** /ratings/adjusted | 
*RatingsApi* | [**get_srs**](docs/RatingsApi.md#get_srs) | **GET** /ratings/srs | 
*RecruitingApi* | [**get_recruits**](docs/RecruitingApi.md#get_recruits) | **GET** /recruiting/players | 
*StatsApi* | [**get_player_season_shooting_stats**](docs/StatsApi.md#get_player_season_shooting_stats) | **GET** /stats/player/shooting/season | 
*StatsApi* | [**get_player_season_stats**](docs/StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
*StatsApi* | [**get_team_season_shooting_stats**](docs/StatsApi.md#get_team_season_shooting_stats) | **GET** /stats/team/shooting/season | 
*StatsApi* | [**get_team_season_stats**](docs/StatsApi.md#get_team_season_stats) | **GET** /stats/team/season | 
*TeamsApi* | [**get_team_roster**](docs/TeamsApi.md#get_team_roster) | **GET** /teams/roster | 
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /teams | 
*VenuesApi* | [**get_venues**](docs/VenuesApi.md#get_venues) | **GET** /venues | 


## Documentation For Models

 - [AdjustedEfficiencyInfo](docs/AdjustedEfficiencyInfo.md)
 - [AdjustedEfficiencyInfoRankings](docs/AdjustedEfficiencyInfoRankings.md)
 - [ConferenceHistory](docs/ConferenceHistory.md)
 - [ConferenceHistoryTeamsInner](docs/ConferenceHistoryTeamsInner.md)
 - [ConferenceInfo](docs/ConferenceInfo.md)
 - [DraftPick](docs/DraftPick.md)
 - [DraftPosition](docs/DraftPosition.md)
 - [DraftTeam](docs/DraftTeam.md)
 - [GameBoxScorePlayers](docs/GameBoxScorePlayers.md)
 - [GameBoxScorePlayersPlayersInner](docs/GameBoxScorePlayersPlayersInner.md)
 - [GameBoxScoreTeam](docs/GameBoxScoreTeam.md)
 - [GameBoxScoreTeamStats](docs/GameBoxScoreTeamStats.md)
 - [GameBoxScoreTeamStatsPoints](docs/GameBoxScoreTeamStatsPoints.md)
 - [GameInfo](docs/GameInfo.md)
 - [GameLineInfo](docs/GameLineInfo.md)
 - [GameLines](docs/GameLines.md)
 - [GameMediaInfo](docs/GameMediaInfo.md)
 - [GameMediaInfoBroadcastsInner](docs/GameMediaInfoBroadcastsInner.md)
 - [GameStatus](docs/GameStatus.md)
 - [LineProviderInfo](docs/LineProviderInfo.md)
 - [LineupStats](docs/LineupStats.md)
 - [LineupUnitStats](docs/LineupUnitStats.md)
 - [LineupUnitStatsFourFactors](docs/LineupUnitStatsFourFactors.md)
 - [LineupUnitStatsTwoPointers](docs/LineupUnitStatsTwoPointers.md)
 - [PlayInfo](docs/PlayInfo.md)
 - [PlayInfoOnFloorInner](docs/PlayInfoOnFloorInner.md)
 - [PlayInfoParticipantsInner](docs/PlayInfoParticipantsInner.md)
 - [PlayTypeInfo](docs/PlayTypeInfo.md)
 - [PlayerSeasonShootingStats](docs/PlayerSeasonShootingStats.md)
 - [PlayerSeasonStats](docs/PlayerSeasonStats.md)
 - [PlayerSeasonStatsWinShares](docs/PlayerSeasonStatsWinShares.md)
 - [PlayerSubsititution](docs/PlayerSubsititution.md)
 - [PlayerSubsititutionSubIn](docs/PlayerSubsititutionSubIn.md)
 - [PollTeamInfo](docs/PollTeamInfo.md)
 - [Recruit](docs/Recruit.md)
 - [RecruitCommittedTo](docs/RecruitCommittedTo.md)
 - [RecruitHometown](docs/RecruitHometown.md)
 - [SeasonShootingStats](docs/SeasonShootingStats.md)
 - [SeasonShootingStatsAttemptsBreakdown](docs/SeasonShootingStatsAttemptsBreakdown.md)
 - [SeasonShootingStatsDunks](docs/SeasonShootingStatsDunks.md)
 - [SeasonType](docs/SeasonType.md)
 - [ShootingStats](docs/ShootingStats.md)
 - [ShotInfo](docs/ShotInfo.md)
 - [ShotInfoLocation](docs/ShotInfoLocation.md)
 - [ShotInfoShooter](docs/ShotInfoShooter.md)
 - [ShotTypeBreakdown](docs/ShotTypeBreakdown.md)
 - [SrsInfo](docs/SrsInfo.md)
 - [TeamInfo](docs/TeamInfo.md)
 - [TeamRoster](docs/TeamRoster.md)
 - [TeamRosterPlayer](docs/TeamRosterPlayer.md)
 - [TeamRosterPlayerHometown](docs/TeamRosterPlayerHometown.md)
 - [TeamSeasonStats](docs/TeamSeasonStats.md)
 - [TeamSeasonUnitStats](docs/TeamSeasonUnitStats.md)
 - [TeamSeasonUnitStatsFieldGoals](docs/TeamSeasonUnitStatsFieldGoals.md)
 - [TeamSeasonUnitStatsFouls](docs/TeamSeasonUnitStatsFouls.md)
 - [TeamSeasonUnitStatsFourFactors](docs/TeamSeasonUnitStatsFourFactors.md)
 - [TeamSeasonUnitStatsPoints](docs/TeamSeasonUnitStatsPoints.md)
 - [TeamSeasonUnitStatsRebounds](docs/TeamSeasonUnitStatsRebounds.md)
 - [TeamSeasonUnitStatsTurnovers](docs/TeamSeasonUnitStatsTurnovers.md)
 - [VenueInfo](docs/VenueInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: Bearer authentication


## Author

admin@collegefootballdata.com


