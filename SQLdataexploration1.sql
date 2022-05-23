select *
from portfolioproject.dbo.CovidDeaths
where continent is not null
order by 3,4

select location,date,total_cases,new_cases,total_deaths,population
from portfolioproject.dbo.CovidDeaths
where continent is not null
order by 1,2

--looking at total cases vs population

select location,date,total_cases,population,(total_cases/population)*100 as cases_percentage
from portfolioproject.dbo.CovidDeaths
where location ='india'and 
continent is not null
order by 1,2

--looking at total_cases vs total_deaths
--shows likelihood of dying if you contract covid in your country

select location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 as death_percentage
from portfolioproject.dbo.CovidDeaths
where location ='india'and
continent is not null
order by 1,2

--looking at countries with highest infection rate

select location,population,max(total_cases) as highestinfectcount,max((total_cases/population))*100 as percentageinfected
from portfolioproject.dbo.CovidDeaths
group by location,population
order by percentageinfected desc

--looking at countries with highest death count

select location,max(cast (total_deaths as int)) as totaldeathcount
from portfolioproject.dbo.CovidDeaths
where continent is not null
group by location
order by totaldeathcount desc


--looking continent wise

select continent,max(cast (total_deaths as int)) as totaldeathcount
from portfolioproject.dbo.CovidDeaths
where continent is not null
group by continent
order by totaldeathcount desc

--global numbers

select sum(new_cases) as totalnewcases,sum(cast(new_deaths as int)) as totalnewdeaths,
sum(cast(new_deaths as int))/sum(new_cases)*100 as deathpercentage
from portfolioproject.dbo.CovidDeaths
where continent is not null
--group by date
order by 1,2


--total poulations vs total vaccinations
--showing percentage of people that has recieved atleast one vaccine dose

select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location,dea.date)
as rollingvaccinatedpeople
--(rollingvacinnatedpeople/population)*100
from portfolioproject.dbo.CovidDeaths as dea
join portfolioproject.dbo.CovidVaccinations as vac
   on dea.location =vac.location
   and dea.date=vac.date
where dea.continent is not null
order by 2,3


-- Using CTE to perform Calculation on Partition By in previous query

with popvsvac (continent,location,date,population,new_vaccinations,rollingpeoplevaccinated)
as
(
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location,dea.date)
as rollingvaccinatedpeople
--(rollingvacinnatedpeople/population)*100
from portfolioproject.dbo.CovidDeaths as dea
join portfolioproject.dbo.CovidVaccinations as vac
   on dea.location =vac.location
   and dea.date=vac.date
where dea.continent is not null
--order by 2,3
)
select *,(rollingpeoplevaccinated/population)*100 as vaccinatedpercent 
from popvsvac


 --Using Temp Table to perform Calculation on Partition By in previous query
 
 drop table if exists #percentpopulationvaccianted
 create table #percentpopulationvaccianted
 (
 Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)


insert into #percentpopulationvaccianted
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location,dea.date)
as rollingvaccinatedpeople
--(rollingvacinnatedpeople/population)*100
from portfolioproject.dbo.CovidDeaths as dea
join portfolioproject.dbo.CovidVaccinations as vac
   on dea.location =vac.location
   and dea.date=vac.date
--where dea.continent is not null
--order by 2,3

select *,(rollingpeoplevaccinated/population)*100 as vaccinatedpercent 
from #percentpopulationvaccianted


--creating view to store data for later visualizations
create view percentPoupulationVaccinated as 
select dea.continent,dea.location,dea.date,dea.population,vac.new_vaccinations,
sum(cast(vac.new_vaccinations as int)) over (partition by dea.location order by dea.location,dea.date)
as rollingvaccinatedpeople
--(rollingvacinnatedpeople/population)*100
from portfolioproject.dbo.CovidDeaths as dea
join portfolioproject.dbo.CovidVaccinations as vac
   on dea.location =vac.location
   and dea.date=vac.date
where dea.continent is not null
--order by 2,3

