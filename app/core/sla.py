import datetime


class SLA:
    """
    SLA Class
    """
    def __init__(self, percent):
        # SLA 계산을 위한 사용자 퍼센티지
        self.percentage = percent

        # 일, 월, 년별 기본 수치값
        self.DAY = 1
        self.SECOND_PER_DAY = 86400
        # Reference: http://en.wikipedia.org/wiki/Year#Summary
        # Reference: http://manse.ndsl.kr/contents-3.html
        # 그레고리력의 1년 평균 길이는365.2425일이다
        self.YEAR = 365.2425
        self.MONTH = self.YEAR / 12

        # SLA 값을 계산할 일별, 주별, 월별, 연별 연산 수치
        self.period = {
            'daily': self.DAY,
            'weekly': self.DAY * 7,
            'monthly': self.MONTH,
            'yearly': self.YEAR,
        }

    def downtime(self) -> dict:
        """
        가동 중지 허용 시간을 계산한다
        :return:
        """
        res = dict()
        # 일자별 Key('daily', 'weekly'..)을 순회하며 가동 중지 시간을 계산한다
        for p in self.period.keys():
            res[p] = self._downtime_calc(self.period[p])

        return res

    def _downtime_calc(self, period: float) -> str:
        """
        일자별 가동 중지 허용 시간을 계산한다
        :param period: 일자별 SLA 값을 계산할 연산 수치(self.day, self.weekly...)
        :return: '0h 0m 0h 0s'
        """
        # 가동율을 분수로 변환한다
        # Ex) SLA 99.9% = 99.9% / 100% = 0.9990000000000001
        uptime_fraction = self.percentage / 100
        # 가동 일자를 초(second) 단위로 변환한다
        second_per_day = self.SECOND_PER_DAY * period
        # 가동 중지가 허용되는 시간을 계산한다
        down_time = second_per_day - (uptime_fraction * second_per_day)

        return self._make_str(down_time)

    @staticmethod
    def _make_str(down_time: float):
        """
        float 시간을 humanize string 으로 변환하여 반환한다
        :param down_time:
        :return:
        """
        # 결과 string을 저장할 변수이다
        dt_str = ""
        # downtime 값을 timedelta로 시간차를 구한다
        td = datetime.timedelta(seconds=down_time)

        days = td.days
        # '일'이 1일 이상인 경우 string에 포함한다
        if days >= 1:
            dt_str += f'{td.days}d '
        # '시간'이 0시간 보다 크다면 string에 포함한다
        hours, remainder = divmod(td.seconds, 3600)
        if hours > 0:
            dt_str += f'{hours}h '
        # '분(minute)'이 0분보다 크다면 string에 포함한다
        minutes, seconds = divmod(remainder, 60)
        if minutes > 0:
            dt_str += f'{minutes}m '

        # '초(second)'는 기본적으로 값이 없어도 string에 포함한다
        seconds += td.microseconds / 1e6
        seconds = int(seconds)
        dt_str += f'{seconds}s'

        return dt_str

