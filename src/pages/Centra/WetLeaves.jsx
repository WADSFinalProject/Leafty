import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import WidgetContainer from '../../components/Cards/WidgetContainer';
import SearchLogo from '../../assets/SearchLogo.svg';
import CircularButton from '../../components/CircularButton';
import WetLeavesLogo from '../../assets/WetLeaves.svg';
import Countdown from '../../components/Countdown';
import InnerPlugins from '../../assets/InnerPlugins.svg';
import CountdownIcon from '../../assets/Countdown.svg';
import ExpiredWarningIcon from '../../assets/ExpiredWarning.svg';
import InputField from '../../components/InputField';
import { Search } from '@mui/icons-material';
import Fab from '@mui/material/Fab';
import AddIcon from '@mui/icons-material/Add';
import Date from '../../assets/Date.svg';
import WeightLogo from '../../assets/Weight.svg';
import PackageCount from '../../assets/Packagecount.svg';
import Drawer from '../../components/Drawer';

function WetLeaves() {
  const [openDrawer, setOpenDrawer] = useState(false);

  const data = [
    { time: "01h05m", color: "#79B2B7", image: CountdownIcon, weight: "30 Kg", code: "W332120", date: "23-21-2024" },
    { time: "01h45m", color: "#79B2B7", image: CountdownIcon, weight: "20 Kg", code: "W261760", date: "24-21-2024" },
    { time: "Expired", color: "#D45D5D", image: ExpiredWarningIcon, weight: "40 Kg", code: "W643210", date: "25-21-2024" },
    { time: "Expired", color: "#D45D5D", image: ExpiredWarningIcon, weight: "40 Kg", code: "W443210", date: "26-21-2024" },
  ];
  

  return (
    <>
      <div className="mt-4 flex justify-center items-center gap-3">
        <InputField icon={SearchLogo} placeholder="Search" className="w-full" />
        <div className='ml-1'>
          <WidgetContainer backgroundColor="#94C3B3" borderRadius="20px" border={false}>
            <img src={InnerPlugins} alt="Inner Plugins" className='w-full h-8' />
          </WidgetContainer>
        </div>
      </div>
      {data.map((item) => (
        <div key={item.code} className='flex justify-between'>
          <WidgetContainer borderRadius="10px" className="w-full flex items-center ">
            <Link to="/centra/wet-leaves/detail">
              <CircularButton imageUrl={WetLeavesLogo} backgroundColor="#94C3B3" />
            </Link>
            <div className='flex flex-col ml-3'>
              <span className="font-montserrat text-base font-semibold leading-tight tracking-wide text-left">
                {item.weight}
              </span>
              <span className='font-montserrat text-sm font-medium leading-17 tracking-wide text-left'>
                {item.code}
              </span>
            </div>
            <div className="flex ml-auto items-center">
              <Countdown time={item.time} color={item.color} image={item.image} />
            </div>
          </WidgetContainer>
        </div>
      ))}
      <Drawer includeFourthSection={false} showThirdInput={false} firstText="Date" secondText="Weight" firstImgSrc={Date} secondImgSrc={WeightLogo}/>
    </>
  );
}

export default WetLeaves;
