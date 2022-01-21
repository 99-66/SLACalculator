# SLA Calculator

SLA Downtime 계산을 위한 API

# SLA(Service Level Agreement)
사전에 정의된 수준의 서비스를 제공하기로 맺는 협약

```shell
Downtime : 기간(daily, monthly..) 중에 서비스를 사용할 수 없는 시간
```
```shell
Uptime : 기간(daily, monthly..) 중에 서비스를 사용할 수 있는 시간
```

서비스 제공업체는 다음 예와 같이 특정 기간에 대한 가동율(퍼센티지)를 보장한다는 것과 같은 내용을 게시

"월별 가동율 99.9%", 이 말은 제공하는 서비스가 월별 가동 시간에 99.9%만큼 서비스를 사용할 수 있게끔 제공한다는 것을 의미
```shell
월별 가동율 99.9%가 허용하는 downtime은 43분 49초이다
```

기간별 가동율 99.9%가 허용하는 downtime
```shell
"daily": "1m 26s"
"weekly": "10m 4s"
"monthly": "43m 49s"
"yearly": "8h 45m 56s"
```

##Optional information
```shell
SLA Calculator 사이트를 보다보면 간혹 같은 99.9%라도 시간 차가 있는 것을 볼 수 있다
- https://uptime.is/
- http://www.slatools.com/sla-uptime-calculator

두 사이트가 같은 가동율에도 시간 차가 발생하는 것은 1년의 일수가 다르기 때문이다
보통 1년을 365일로 계산하지만, 그레고리력으로 1년의 평균 길이는 365.2425일이 된다
(* https://en.wikipedia.org/wiki/Year#Summary 중
"An average Gregorian year is 365.2425 days"...)
 
따라서 1년을 어떤 일수로 두냐에 따라 다음과 같이 Yearly downtime에 차이가 발생하게 된다
1년을 365.2425으로 계산 : 8h 45m 56s
1년을 365으로 계산 : 8h 45m 35s
```

## SLA API
퍼센티지를 파라미터로 받아 가동율에 대한 downtime을 반환한다
> https://api.slx.sh/sla/{percentage}

> Example: https://api.slx.sh/sla/99.9

```shell
{
  "daily": "1m 26s",
  "weekly": "10m 4s",
  "monthly": "43m 49s",
  "yearly": "8h 45m 56s"
}
```

## API Docs
> **Swagger**: https://api.slx.sh/docs

> **ReDoc**: https://api.slx.sh/redoc


## Deployed platform
- [Deta](https://www.deta.sh/)
